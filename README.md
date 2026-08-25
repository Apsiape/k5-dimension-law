# The dimension cost of approximating a non-attained quantum correlation: a Diophantine law for $K_5$

**The paper: [paper/PAPER-K5.md](paper/PAPER-K5.md)** — *"How much dimension
does an $\varepsilon$-approximation to a non-attained quantum correlation cost?
A Diophantine answer for $K_5$"* (v1.0.0). Statement, proofs, conventions,
priority discussion and verification appendix.

---

## Claim boundaries, stated first

Before the claims, the fences around them. Each of these is stated in the paper
too, at the point where it bites.

- **One parameter, one witness.** The law below is proved at the single
  distinguished parameter $t_\ast = 1/\sqrt5$ of the Dykema–Paulsen–Prakash
  $K_5$ non-closure witness. §5.4 gives the shape of the general answer for
  quadratic irrationals, but that two-parameter formula is *stated, not proved*;
  its ingredients are proved here only for $\sqrt5$.
- **Exact marginals are load-bearing, and the drifted problem is open.** Every
  result assumes the carrier's marginals are exactly $t_\ast$. If the marginals
  may drift by $\delta$, the Diophantine obstruction can be voided. The
  conjectural $\Theta(\min(\varepsilon^{-1/4},\delta^{-1/2}))$ law of §5.3 is
  **not proved and not claimed**. This is the one place the paper's regime is
  genuinely narrower than the physical question.
- **The constant is bracketed, not pinned.** $D(\varepsilon)$ is a minimum over
  *all* finite-dimensional carriers. $0.9732489895$ is the sharpest constant so
  far *attained*, by an explicit family; it is not a matching lower bound.
  Nothing here rules out a better carrier at a given $\varepsilon$.
- **Conventions are not interchangeable.** Three dimension conventions are in
  use (§5.1) and the constants differ between them by up to an order of
  magnitude. The headline bracket $2.176$ is in the *denominator* convention.
  Do not cross it with the actual-dimension figures.
- **One secondary citation.** Lemma 4.7 ($d_5(p/q) = q$) is attributed to
  [KRS03] via [Shu07] and is labelled SECONDARY throughout: the source was not
  obtained in full. The paper's own statement, Lemma 4.6 ($q \le d_5(p/q) \le
  2q$), is proved without it. This is the sole reason Cor. 4.8 reports an
  interval $4.866 \le C_{\mathrm{act}} \le 9.732$ rather than a value. §7.3
  discloses both documents that could not be read in full.
- **Priority is provisional.** "New, provisional" means *no evidence found*, not
  *proved absent*. §7.2 reports the sweep as it actually ran, including one
  component (a citing-set enumeration) that is disclosed as supporting evidence
  rather than a reproducible check, because its API, query and date were not
  snapshotted.
- **Some claims are not machine-checked, and are named.** §5.2's uniform constant
  in actual dimension, §5.3's Open Lemma, §5.4's Liouville-exponent remark,
  Lemma 4.7, Cor. 4.8's interval, and all of §7.1's comparison numbers. Table 8.1
  marks each *not checked* in place.

## What is proved

Dykema, Paulsen and Prakash showed that the finite-dimensional quantum
correlation set $C_q(5,2)$ is not closed, using a $K_5$ graph correlation
function whose infimum is not attained at irrational parameters in an explicit
window. Their argument is **existential in dimension**: the carriers it invokes
live "in $M_k$ for some natural number $k$", with no control on $k$, and no
approximating sequence, rate or carrier is written down at the non-attained
parameter.

This paper answers the quantitative question that leaves open. Let
$D(\varepsilon)$ be the least block dimension of a finite-dimensional carrier
whose value exceeds the infimum by at most $\varepsilon$, at exact marginals and
at $t_\ast = 1/\sqrt5$. Then

```text
D(eps) = Theta(eps^(-1/4))
```

and the exponent is **arithmetic in origin**, not dynamical.

**Both directions, with constants.**

| direction | statement | constant | status |
|---|---|---|---|
| lower (Theorem A) | every carrier at exact marginals has deficit $\varepsilon > 1/(25Q^4)$, $Q$ the largest reduced denominator of a block value | $Q\varepsilon^{1/4} > 25^{-1/4} = 0.4472135955$ | **unconditional**; no block-scalar assumption, no equal-rank assumption, no bound on the number of blocks |
| upper (Theorem B) | two-block carriers from consecutive continued-fraction convergents of $\sqrt5$ | $N\varepsilon^{1/4} \to ((2+\sqrt5)/(2\sqrt5))^{1/2} = 0.9732489895$ | **attained** along an explicit family, in exact arithmetic |

**The constants bracket the law to a factor $2.176$**, both ends in the
*denominator* convention, where both are proved directly:
$0.4472135955 \le \cdot \le 0.9732489895$. The exponent $-1/4$ holds in all
three dimension conventions of §5.1; only the constant moves (in actual block
dimension the corresponding bracket is a factor $10.9$–$21.8$).

**Why the exponent is $-1/4$.** The lower bound is the Diophantine inequality
$\lVert q\sqrt5\rVert > 1/(5q)$ transported through the law of total variance:
the approximation deficit *is* $\mathrm{Var}_\tau(S)$, and only the
block-averaged data survives, which is forced to be rational. The upper bound
comes from an exact identity — for a two-block carrier the deficit is the
**product of the two one-sided approximation errors**,
$\varepsilon = (\lambda_1-\sqrt5)(\sqrt5-\lambda_2)$ — which turns the problem
into two-sided rational approximation, whose extremisers are the convergents.
Two irrationality exponents multiply; hence the fourth root.

**Two structural results accompany the law.**

- *Orbit topology and attainment are different invariants* (§6). The attained
  parameter $\lambda = 4/3$ has a $\Phi_5$-orbit conjugate to that of the
  unattained $\lambda = \sqrt5$, with the *same* multiplier $\varphi^{-4}$
  exactly. So no topological or dynamical invariant of the orbit — closure,
  termination under descent, periodicity, multiplier, $SL_2$-conjugacy class —
  decides attainment. Attainment is arithmetic; orbit type is the sign of the
  Tits form. This is a clarifying negative result, included because it is the
  first thing one is tempted to believe here and it is false.
- *Dimension laws for non-closure witnesses are not a single phenomenon* (§7.1).
  The analogous cost for the $I_{3322}$ Bell functional is only *logarithmic*.
  Both objects carry a $2\times2$ unimodular transfer operator with a geometric
  multiplier, and the multipliers do not predict the law. What predicts it is the
  arithmetic of the parameter at which attainment fails.

**Not ours, and used as its authors built it:** the star-quiver Coxeter functor
$\Phi_5$ (Kruglyak), the window $[(5-\sqrt5)/2,(5+\sqrt5)/2]$ and the
realisability trichotomy (Kruglyak–Rabanovich–Samoĭlenko), the non-closure of
$C_q(5,2)$ and its limiting correlation (Dykema–Paulsen–Prakash), and the trace
obstruction $q \mid d$, which is folklore. §1.4 tabulates recovery against new,
and §7.4 pre-empts the folklore objection explicitly.

## The verification stack

Stated here exactly as the paper's §8 states it, including what it does *not*
cover.

Three engines are supplied under [`verification/`](verification/). All checks
are in exact arithmetic — `Fraction` over $\mathbb{Q}$, the real quadratic field
$\mathbb{Q}(\sqrt5)$, the cyclotomic field $\mathbb{Q}(\zeta_5)$, exact integers,
and 80-digit `Decimal` where a real number must be compared to a printed
constant — with the single deliberate exception of check C17, which *exhibits*
the failure of floating point on this problem.

| script | what it certifies | checks | status |
|---|---|---|---|
| `verification/verify_dimension_law.py` | §§2–6: setup, Theorem A, Theorem B, §5.4, §6 | C1–C26 (43 assertions) | exit 0 |
| `verification/verify_krs_dimension.py` | Lemma 4.5 ($\dim = 2l$, 7 921 cases); independent re-derivation of the §4.2 table over $\mathbb{Q}$ | K1–K5 (6 assertions) | exit 0 |
| `verification/verify_transport_dimension.py` | Lemma 4.6 ($d \le 2q$ across the window, 4 000 cases, reduction into $[3/2,2]$) | T1–T3 (4 assertions) | exit 0 |

**The architecture, disclosed rather than advertised.** Engines 2 and 3 use only
$\mathbb{Q}$: they do not use the quadratic or cyclotomic arithmetic of engine 1,
and engine 3 contains no floating point at all — its window test is the exact
integer condition $p^2 - 5pq + 5q^2 \le 0$. The three engines are **not mutually
independent**: engine 3's base-interval dimension $2l$ *is* engine 2's
conclusion, so engine 3 is *sequential* on engine 2, not a second opinion about
it.

Left there, a paper selling exact verification would have had **no** claim
checked twice. Engine 2 therefore additionally re-derives the §4.2 table
(checks K4–K5) from scratch by rational interval arithmetic: it brackets
$\sqrt5$ between consecutive convergents to 60-plus digits and bounds each
$\varepsilon$ and each $N\varepsilon^{1/4}$ by comparisons of integers, never
forming an element of $\mathbb{Q}(\sqrt5)$ and never calling `Decimal`.

So: **the §4.2 table and the six-figure plateau of Theorem B are the one
load-bearing claim of this paper that is certified by two engines sharing no
number representation and no verification code.** The one ingredient the two
routes *do* share is the convergent recursion that generates the $\lambda$
pairs themselves. That is disclosed here, in the paper, and in the engines' own
docstrings, because a shared ingredient inside a claimed two-engine check is
exactly the thing a reader is entitled to be told about.

**What the stack does not cover**, labelled *not checked* in Table 8.1 of the
paper: §5.2's uniform constant in actual dimension; §5.3's Open Lemma (unproved
by construction); §5.4's Liouville-exponent remark; all of §7.1's $I_{3322}$
numbers; Lemma 4.7 (a secondary citation); and Cor. 4.8's $4.866$–$9.732$
interval (a consequence of two lemmas, not a computation). Prose, attributions,
and the proofs of Lemmas 4.5 and 4.6 are of course not machine checks either;
the engines confirm their conclusions.

**A warning that is in the paper on purpose** (§8.2). The deficits in the §4.2
table are exact elements of $\mathbb{Q}(\sqrt5)$ of the form $a + b\sqrt5$ with
$a,b$ of size $O(1)$ and $a + b\sqrt5 \approx 10^{-20}$. Evaluating them as
`float(a) + float(b)*sqrt(5)` suffers total cancellation below
$\varepsilon \approx 10^{-13}$: the last three table rows come out as
$1.1236$, $0.0000$, $20.1620$ instead of $0.973249$ — a "result" that reads as
a spectacular breakdown of the law at large $N$. Check C17 reproduces that
failure deliberately, because it occurs *exactly at the regime the theorem is
about*, where a casual verification is most likely to be attempted and most
likely to mislead.

## How to run the engines

Python 3.9 or later, **standard library only** — no `numpy`, no `sympy`, no
`mpmath`, nothing to install.

```sh
cd verification
python verify_dimension_law.py
python verify_krs_dimension.py
python verify_transport_dimension.py
```

or in one line:

```sh
cd verification && python verify_dimension_law.py && python verify_krs_dimension.py && python verify_transport_dimension.py
```

Each prints one `[PASS]`/`[FAIL]` line per check, a summary count, and exits `0`
on a full pass and `1` otherwise. Expect `43`, `6` and `4` assertions
respectively. Total runtime is on the order of 20 seconds, dominated by engine
2's exhaustive 7 921-case recursion; timings are machine-dependent and are
reported, not asserted.

## Review record

The full refereeing history is in [`review/`](review/), with a protocol preface
at [`review/README.md`](review/README.md): two refutation-first blind rounds
either side of a repair round, mutation testing of the checks, and freeze checks
on the reviewed state.

26 findings raised, 26 repaired, 0 dissents; 24 of 26 confirmed faithful on
audit, one honest substitution, one softening reopened and closed, zero missing,
zero overcorrected; four residual conditions raised in the confirm round and all
four discharged. Final ruling: **PROMOTE**.

## On corrections

No arithmetic in this paper was found to be wrong in any review round. What the
rounds killed was the paper *misdescribing its own arithmetic and its own
engines*: a flatness claim ("flat to six figures from $N=17$") that the paper's
own table contradicted two lines below it; a constant bracket that silently
crossed two different dimension conventions; a printed constant wrong in its
fifth significant figure, waved through by a check whose tolerance was too loose
to see it; an engine test that did not test what its lemma claimed; check labels
that promised more than their assertions delivered; a citing-set sweep that could
not be reproduced because its query was never recorded.

Every one of those is corrected in the text you are reading, and every one is
still legible in `review/`. That is the intent. A result whose error history has
been tidied away is a result you have to take on trust; a result whose error
history ships with it can be checked. The corrections are not an embarrassment
attached to the work — they are the reason the surviving statements are worth
something, and they are why claims here carry explicit scope labels
(*unconditional*, *secondary*, *not checked*, *not proved and not claimed*)
rather than a uniform tone of confidence.

If you find an error, it belongs in this record too.

## Citing

See [`CITATION.cff`](CITATION.cff). Version 1.0.1. Concept DOI (all versions):
[10.5281/zenodo.21876896](https://doi.org/10.5281/zenodo.21876896); v1.0.1
version DOI:
[10.5281/zenodo.22099141](https://doi.org/10.5281/zenodo.22099141) —
note: this record's Zenodo metadata carries the stale version string
"1.0.0" from the `.zenodo.json` shipped at tag time (fixed in this
commit for future releases); its archive is the v1.0.1 tree, which
contains the Section 7.2 correction. v1.0.0 version DOI:
[10.5281/zenodo.21876899](https://doi.org/10.5281/zenodo.21876899).

## Licence

Dual, by file type — see [`LICENSE.md`](LICENSE.md). Prose and the paper are
**CC BY 4.0**; the verification engines are **MIT**.
