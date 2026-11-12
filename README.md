# The dimension cost of approximating a non-attained quantum correlation: a Diophantine law for $K_5$

**The paper: [paper/PAPER-K5.md](paper/PAPER-K5.md)** — *"How much dimension
does an $\varepsilon$-approximation to a non-attained quantum correlation cost?
A Diophantine answer for $K_5$"* (v1.1.0). Statement, proofs, conventions,
priority discussion and verification appendix.

---

## Changes in 1.1.0

Version 1.1.0 (2026-11-11) determines the denominator problem exactly. Full
notes: [`RELEASE-NOTES-v1.1.0.md`](RELEASE-NOTES-v1.1.0.md).

- **Exact Farey law** (§4.2a, Theorem B1). In the denominator convention the
  minimum deficit over all carriers whose block values have reduced
  denominators $\le Q$ is $e_Q=(a_Q-\sqrt5)(\sqrt5-b_Q)$, where
  $b_Q<\sqrt5<a_Q$ are the Farey neighbours of order $Q$, and
  $D_{\rm den}(\varepsilon)=\min\{Q:e_Q\le\varepsilon\}$. A supporting-line
  identity proves the bound for every carrier (non-scalar blocks, any number of
  blocks, mixed denominators); two scalar neighbour blocks attain it.
- **Sharp constants** (Cor. B2). As $\varepsilon\downarrow0$,
  $\liminf D_{\rm den}(\varepsilon)\varepsilon^{1/4}=L=(4/(5\varphi^2))^{1/4}\approx0.7434960689$
  and
  $\limsup D_{\rm den}(\varepsilon)\varepsilon^{1/4}=U=(\varphi^{10}/20)^{1/4}\approx1.5747499445$.
  They are limits, not uniform bounds.
- **Exact drift law** (Theorem 5.3(b,c)). A carrier with reduced denominators
  $\le Q$, marginal drift $\le\delta$ and fixed-target deficit
  $\le\varepsilon$ exists if and only if
  $e_Q\le\varepsilon+5(a_Q+b_Q-1)\delta$. The pure-drift liminf constant is
  $\approx0.3642394613$ (limsup $\approx0.7714715591$), below the convergent
  family's $0.4767956449$.
- **$\sqrt5$ against $\varphi$** (§5.4). At $\varphi$ the sharp constants are
  $\approx0.8506508084$ and $\approx1.3763819205$: a higher best case and a
  lower worst case than at $\sqrt5$.
- **Three corrections to v1.0.2 statements** (details under
  [On corrections](#on-corrections)): v1.0.2's §4.1 and §5.3 called the
  convergents the extremisers, and its §5.2 called the convergent deficit ratio
  an exact fixed factor.
- **Two new engines**, `verify_farey_field.py` and
  `verify_farey_intervals.py` (§8.3), sharing no number representation. The
  three original engines are unchanged.
- **Unchanged:** the exponent $-1/4$ in every dimension convention, Theorem A,
  Theorem B's convergent family and its tables, and the v1.0.2 drift
  correction.

## Claim boundaries, stated first

Before the claims, the fences around them. Each of these is stated in the paper
too, at the point where it bites.

- **One parameter, one witness.** The law below is proved at the single
  distinguished parameter $t_\ast = 1/\sqrt5$ of the Dykema–Paulsen–Prakash
  $K_5$ non-closure witness. §5.4 compares the sharp constants at $\sqrt5$ and
  $\varphi$; no general formula is claimed.
- **Exact marginals are load-bearing, and the drifted problem is settled.**
  Every result of §§3–4 assumes the carrier's marginals are exactly
  $t_\ast$. If the marginals may drift by $\delta$, the cost against the fixed
  target is $\Theta(\min(\varepsilon^{-1/4},\delta^{-1/4}))$ (Theorem 5.3): the
  same fourth root, **not** the $\delta^{-1/2}$ that v1.0.0–1.0.1 conjectured
  in an Open Lemma. That conjecture was false: an explicit two-block carrier at
  denominator $17$ has deficit exactly zero with marginals off by
  $6\times10^{-7}$. In the denominator convention the drift threshold is exact
  (Theorem 5.3(c)). The $\delta^{-1/2}$ form survives only for a deficit
  referenced to the carrier's own mean (Prop. 5.4).
- **The denominator law is exact (v1.1.0).**
  $D_{\rm den}(\varepsilon)=\min\{Q:e_Q\le\varepsilon\}$,
  $e_Q=(a_Q-\sqrt5)(\sqrt5-b_Q)$; liminf/limsup of
  $D_{\rm den}\varepsilon^{1/4}$ are $0.7434960689\ldots$/$1.5747499445\ldots$
  (limits, not uniform bounds); $D_{\rm den}\le D\le2D_{\rm den}$ (Lemma 4.6).
  Exact constants in actual block dimension and in total Hilbert dimension are
  not claimed.
- **Conventions are not interchangeable.** Three dimension conventions are in
  use (§5.1) and the constants differ between them by up to an order of
  magnitude. The sharp constants $L$ and $U$ are in the *denominator*
  convention. On primary evidence actual block dimension is within a factor
  $2$ of it and total Hilbert dimension within a factor $20$
  ($D_{\rm den}\le D_{\rm tot}\le20D_{\rm den}$). Do not cross the conventions.
- **One secondary citation.** Lemma 4.7 ($d_5(p/q) = q$) is attributed to
  [KRS03] via [Shu07] and is labelled SECONDARY throughout: the source was not
  obtained in full. The paper's own statement, Lemma 4.6 ($q \le d_5(p/q) \le
  2q$), is proved without it. This is the sole reason actual block dimension is
  bounded by $D_{\rm den}\le D\le2D_{\rm den}$ rather than shown equal to
  $D_{\rm den}$, and the sole reason Cor. 4.8 places the limit points of its
  merged equal-rank family in $[4.866, 9.732]$ rather than giving a value. §7.3
  discloses both documents that could not be read in full.
- **Priority is provisional.** "New, provisional" means *no evidence found*, not
  *proved absent*. §7.2 reports the sweep as it actually ran, including one
  component (a citing-set enumeration) that is disclosed as supporting evidence
  rather than a reproducible check, because its API, query and date were not
  snapshotted. The v1.1.0 additions carry the same label; their
  Farey/Stern–Brocot ingredients are classical.
- **Some claims are not machine-checked, and are named.** Lemma 4.7, Cor. 4.8's
  interval, the actual- and total-dimension comparisons of §5.1 (proved from
  Lemma 4.6, not computed), and all of §7.1's comparison numbers. The exact
  Farey law, its limiting constants and the drift criterion are proved in the
  text; the engines confirm finite instances and do not replace the universal
  statements. Table 8.1 gives the status of each claim in place.

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

**In denominators the law is exact.** Write $Q$ for the largest reduced
denominator of a block value and $D_{\rm den}$ for the corresponding minimum.
If $b_Q<\sqrt5<a_Q$ are the Farey neighbours of order $Q$ (the nearest
rationals of denominator $\le Q$ on either side of $\sqrt5$), then

```text
e_Q = (a_Q - sqrt5)(sqrt5 - b_Q),        D_den(eps) = min{ Q : e_Q <= eps },

liminf D_den(eps) eps^(1/4) = (4/(5 phi^2))^(1/4) ~ 0.7434960689
limsup D_den(eps) eps^(1/4) = (phi^10/20)^(1/4)   ~ 1.5747499445
```

(§4.2a: Theorem B1 and Cor. B2). The liminf is approached along the
intermediate semiconvergent pairs at $Q=21,89,377,\ldots$; the limsup at
tolerances just below the $j=3$ plateau heights, where the next convergent
denominator is required. Both are limits, not uniform bounds: at
$\varepsilon=e_{21}$, $D_{\rm den}\varepsilon^{1/4}=0.74321\ldots<L$.

**The results, with constants.**

| result | statement | constant | status |
|---|---|---|---|
| lower (Theorem A) | every carrier at exact marginals has deficit $\varepsilon > 1/(25Q^4)$, $Q$ the largest reduced denominator of a block value | $Q\varepsilon^{1/4} > 25^{-1/4} = 0.4472135955$ | **unconditional** and uniform; no block-scalar assumption, no equal-rank assumption, no bound on the number of blocks; valid but not sharp |
| exact minimum (Theorem B1) | every carrier with reduced denominators $\le Q$ has $\varepsilon\ge e_Q$; two scalar Farey-neighbour blocks attain it | liminf $0.7434960689$, limsup $1.5747499445$ of $D_{\rm den}\varepsilon^{1/4}$ | **proved for every carrier**, with the same generality as Theorem A; sharp |
| upper (Theorem B) | two-block carriers from consecutive continued-fraction convergents of $\sqrt5$ | $N\varepsilon^{1/4} \to ((2+\sqrt5)/(2\sqrt5))^{1/2} = 0.9732489895$ | **attained** along an explicit family, in exact arithmetic; valid but not optimal |

**The denominator law is exact** (§4.2a); Theorem B's convergent value
$0.9732489895$ is valid but not optimal. The exponent $-1/4$ holds in all
three dimension conventions of §5.1; only the constant moves. On primary
evidence $D_{\rm den}\le D\le2D_{\rm den}$ and
$D_{\rm den}\le D_{\rm tot}\le20D_{\rm den}$; under the secondary Lemma 4.7,
$D=D_{\rm den}$.

**Why the exponent is $-1/4$.** The lower bound is the Diophantine inequality
$\lVert q\sqrt5\rVert > 1/(5q)$ transported through the law of total variance:
the approximation deficit *is* $\mathrm{Var}_\tau(S)$, and only the
block-averaged data survives, which is forced to be rational. The upper bound
comes from an exact identity — for a two-block carrier the deficit is the
**product of the two one-sided approximation errors**,
$\varepsilon = (\lambda_1-\sqrt5)(\sqrt5-\lambda_2)$ — which turns the problem
into two-sided rational approximation, whose minimisers at each denominator
bound are the Farey neighbours of $\sqrt5$, intermediate semiconvergents
included. Two irrationality exponents multiply; hence the fourth root. For an
arbitrary carrier the picture is exact: with trace weights $\lambda_l$ and block
means $s_l$,
$\varepsilon-e_Q=\sum_l\lambda_l\mathrm{Var}_{\mathrm{tr}}(S_l)+\sum_l\lambda_l(s_l-a_Q)(s_l-b_Q)\ge0$,
because no admissible block mean lies strictly between the two neighbours.

**The drift law is exact in denominators.** If each marginal may drift by at
most $\delta$, a carrier with reduced denominators $\le Q$ and fixed-target
deficit $\le\varepsilon$ exists if and only if
$e_Q\le\varepsilon+5(a_Q+b_Q-1)\delta$ (Theorem 5.3(c)). At zero deficit the
least drift at order $Q$ is $e_Q/(5(a_Q+b_Q-1))$, and
$D_{\rm den}(0,\delta)\delta^{1/4}$ has liminf $\approx0.3642394613$ and limsup
$\approx0.7714715591$ (Theorem 5.3(b)). In every convention
$D(\varepsilon,\delta)=\Theta(\min(\varepsilon^{-1/4},\delta^{-1/4}))$, with
Theorem 5.3(a)'s unconditional lower bound.

**$\sqrt5$ against $\varphi$** (§5.4). The same supporting-line proof at
$\varphi=(1+\sqrt5)/2$ gives the sharp constants
$(\varphi/\sqrt5)^{1/2}\approx0.8506508084$ and
$\varphi(\varphi/\sqrt5)^{1/2}\approx1.3763819205$. So $\varphi$ is harder than
$\sqrt5$ in the best asymptotic case and cheaper in the worst: neither
parameter is uniformly ordered by these constants.

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
$C_q(5,2)$ and its limiting correlation (Dykema–Paulsen–Prakash), the trace
obstruction $q \mid d$, which is folklore, and the Farey/Stern–Brocot
neighbour structure used in §4.2a, which is classical. §1.4 tabulates recovery
against new, and §7.4 pre-empts the folklore objection explicitly.

## The verification stack

Stated here exactly as the paper's §8 states it, including what it does *not*
cover.

Five engines are supplied under [`verification/`](verification/): the three
original engines, and two added in v1.1.0 for the exact Farey law (§8.3). The
original engines' checks are in exact arithmetic — `Fraction` over
$\mathbb{Q}$, the real quadratic field $\mathbb{Q}(\sqrt5)$, the cyclotomic
field $\mathbb{Q}(\zeta_5)$, exact integers, and 80-digit `Decimal` where a
real number must be compared to a printed constant — with the single deliberate
exception of check C17, which *exhibits* the failure of floating point on this
problem. The Farey engines use exact $\mathbb{Q}(\sqrt5)$ arithmetic with
180-digit `Decimal` for limit comparisons (engine A) and integer square-root
enclosures with certified rational intervals (engine B, which uses `float` only to
format printed approximations).

| script | what it certifies | checks | status |
|---|---|---|---|
| `verification/verify_dimension_law.py` | §§2–6: setup, Theorem A, Theorem B, §5.3, §5.4, §6 | C1–C29 (48 assertions) | exit 0 |
| `verification/verify_krs_dimension.py` | Lemma 4.5 ($\dim = 2l$, 7 921 cases); independent re-derivation of the §4.2 table over $\mathbb{Q}$ | K1–K5 (6 assertions) | exit 0 |
| `verification/verify_transport_dimension.py` | Lemma 4.6 ($d \le 2q$ across the window, 4 000 cases, reduction into $[3/2,2]$) | T1–T3 (4 assertions) | exit 0 |
| `verification/verify_farey_field.py` (engine A, v1.1.0) | §§4.2a, 5.3, 5.4 in $\mathbb{Q}(\sqrt5)$: all reduced support means in $[0,5]$ at orders 1–12 (42,519 straddling pairs per objective, deficit and zero-deficit drift); Stern–Brocot nodes through 300,000 (34 for $\sqrt5$, 26 for $\varphi$); drift roots; node limits $L_j$, $U_j$ and the $\varphi$ limits | registered predictions; positive controls $e_4$, $e_{17}$, $\delta_{17}$; a planted non-neighbour pair must lose | exit 0 |
| `verification/verify_farey_intervals.py` (engine B, v1.1.0) | the same minima by certified rational intervals (no field class, no `Decimal`); a per-denominator scan of 300,000 denominators per parameter; independent mediant generation and interval recertification of 100 large-node records through $Q=4\,472\,197\,161\,895\,732$ | registered predictions; the same controls | exit 0 |

**The architecture, disclosed rather than advertised.** Engines 2 and 3 use only
$\mathbb{Q}$: they do not use the quadratic or cyclotomic arithmetic of engine 1,
and engine 3 contains no floating point at all — its window test is the exact
integer condition $p^2 - 5pq + 5q^2 \le 0$. The three original engines are
**not mutually independent**: engine 3's base-interval dimension $2l$ *is*
engine 2's conclusion, so engine 3 is *sequential* on engine 2, not a second
opinion about it.

Left there, a paper selling exact verification would have had **no** claim
checked twice. Engine 2 therefore additionally re-derives the §4.2 table
(checks K4–K5) from scratch by rational interval arithmetic: it encloses
$\sqrt5$ between consecutive convergents to 60-plus digits and bounds each
$\varepsilon$ and each $N\varepsilon^{1/4}$ by comparisons of integers, never
forming an element of $\mathbb{Q}(\sqrt5)$ and never calling `Decimal`.

So: **the §4.2 table and the six-figure plateau of Theorem B are a legacy
load-bearing claim of this paper certified by two engines sharing no number
representation and no verification code.** The one ingredient the two
routes *do* share is the convergent recursion that generates the $\lambda$
pairs themselves. That is disclosed here, in the paper, and in the engines' own
docstrings, because a shared ingredient inside a claimed two-engine check is
exactly the thing a reader is entitled to be told about. The legacy engines are
shipped unchanged; the printed labels of C15, C16, C25 and C26 keep the v1.0
wording, which §§4.2a, 5.2 and 5.4 of the paper supersede.

**The v1.1.0 Farey engines.** Engine A works in $\mathbb{Q}(\sqrt5)$ exactly.
Engine B never forms an element of $\mathbb{Q}(\sqrt5)$: it encloses $\sqrt5$
between two rationals of denominator $10^{180}$, found by an integer square
root, and compares by rational intervals. It
reads engine A's output `engine_a.json` and re-derives every pair count, winner
and node independently: it finds neighbour changes by a per-denominator scan
rather than A's mediant path, regenerates the large nodes by unit mediants
rather than A's convergent recursion, and certifies A's recorded decimal values by
intervals. These finite computations confirm the analytic proofs of §§4.2a, 5.3
and 5.4; they do not replace their universal quantifiers. For the deficit the
enumeration is the entire block-mean relaxation (two-point extreme measures);
for drift it covers straddling pairs, and Theorem 5.3(c)'s proof covers all
supports.

**What the stack does not cover**, as stated in Table 8.1 of the paper: Lemma
4.7 (a secondary citation); Cor. 4.8's $4.866$–$9.732$ interval (a consequence
of two lemmas, not a computation); the actual- and total-dimension comparisons
of §5.1 (proved from Lemma 4.6 and unmerged cyclic copies, not computed); and
all of §7.1's $I_{3322}$ numbers. Prose, attributions, and the proofs of Lemmas
4.5 and 4.6 and of §§4.2a, 5.3 and 5.4 are of course not machine checks either;
the engines confirm their conclusions on finite ranges.

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
`mpmath`, nothing to install. Every engine runs on any platform.

```sh
cd verification
python verify_dimension_law.py
python verify_krs_dimension.py
python verify_transport_dimension.py
python -B verify_farey_field.py
python -B verify_farey_intervals.py
```

or in one line:

```sh
cd verification && python verify_dimension_law.py && python verify_krs_dimension.py && python verify_transport_dimension.py && python -B verify_farey_field.py && python -B verify_farey_intervals.py
```

Each original engine prints one `[PASS]`/`[FAIL]` line per check, a summary
count, and exits `0` on a full pass and `1` otherwise. Expect `48`, `6` and `4`
assertions respectively. Their total runtime is on the order of 20 seconds,
dominated by engine 2's exhaustive 7 921-case recursion.

The two Farey engines must run in that order: `verify_farey_field.py` writes
`engine_a.json`, which `verify_farey_intervals.py` reads before writing
`engine_b.json`, both next to the scripts. They stop with an `AssertionError`
on any failure, and on a full pass print `ALL ENGINE A CHECKS PASS` and
`ALL ENGINE B CHECKS PASS` and exit `0`; expect `BRUTE TOTAL: 42519` and
`PAIR COUNT: 42519 epsilon + 42519 drift`. Each needs about 15 MB of memory
and 2–3 seconds. The shipped `engine_a.json` and `engine_b.json` are the
release run's (`python -I -B`), with its printed transcripts in
`verify_farey_field.stdout.txt` and `verify_farey_intervals.stdout.txt`.
Timings are machine-dependent and are reported, not asserted.

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

**v1.1.0 (2026-11-11): three v1.0.2 sentences were false as written.** None of
them touches a theorem; each misdescribed the extremal structure.

- v1.0.2's §4.1 said the extremisers of the two-sided approximation problem are
  the continued-fraction convergents. At $Q=21$ the optimum is
  $(47/21,38/17)$, whose deficit is below that of the best convergent pair
  $(9/4,38/17)$; already at $Q=5$ the optimum $(9/4,11/5)$ is not a convergent
  pair. The extremisers are the Farey neighbours, intermediate semiconvergents
  included (Theorem B1).
- v1.0.2's §5.3 said the convergents are again the extremisers for drift. At
  $Q=21$ the Farey pair needs drift $9.03\times10^{-8}$ for zero deficit, the
  convergent pair $6.19\times10^{-7}$. Theorem 5.3(c) gives the exact
  threshold.
- v1.0.2's §5.2 said consecutive convergent deficits differ by the fixed factor
  $(2+\sqrt5)^4$. That is only their limit; the exact ratios are $305.05$,
  $322.997$, $321.941$, ….

The convergent tables and constants remain valid as a nonoptimal control
family. See [`RELEASE-NOTES-v1.1.0.md`](RELEASE-NOTES-v1.1.0.md); the
historical release notes keep their original text, with dated addenda.

**v1.0.2 (2026-09-24): the Open Lemma of §5.3 was false.** Versions 1.0.0–1.0.1
conjectured, explicitly unproved and unclaimed, that letting the marginals drift
by $\delta$ costs $\delta^{-1/2}$. It costs $\delta^{-1/4}$ — the same fourth
root as the deficit — against the fixed target the paper defines. The refuting
carrier is a two-block straddling pair at denominator $17$ whose deficit is
exactly zero with marginals off by $6\times10^{-7}$, and the corrected law is
proved in both directions (Theorem 5.3, checks C27–C29). Found while
transporting §§3–4 to another five-projection problem; see
[`RELEASE-NOTES-v1.0.2.md`](RELEASE-NOTES-v1.0.2.md).

## Citing

See [`CITATION.cff`](CITATION.cff). Version 1.1.0 version DOI:
[10.5281/zenodo.24148371](https://doi.org/10.5281/zenodo.24148371). Concept DOI (all versions):
[10.5281/zenodo.21876896](https://doi.org/10.5281/zenodo.21876896); v1.0.2
version DOI:
[10.5281/zenodo.22944181](https://doi.org/10.5281/zenodo.22944181); v1.0.1
version DOI:
[10.5281/zenodo.22099141](https://doi.org/10.5281/zenodo.22099141) —
note: this record's Zenodo metadata carries the stale version string
"1.0.0" from the `.zenodo.json` shipped at tag time (fixed for later
releases); its archive is the v1.0.1 tree, which contains the Section 7.2
correction. v1.0.0 version DOI:
[10.5281/zenodo.21876899](https://doi.org/10.5281/zenodo.21876899).

## Licence

Dual, by file type — see [`LICENSE.md`](LICENSE.md). Prose and the paper are
**CC BY 4.0**; the verification engines are **MIT**.
