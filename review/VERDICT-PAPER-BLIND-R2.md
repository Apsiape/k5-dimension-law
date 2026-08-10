# VERDICT — blind referee round 2 (confirm round), `PAPER-K5.md`

> **Redaction note, 2026-08-10.** This review document was produced inside a
> private working repository. Filesystem paths, repository-internal directory
> names, workspace locations and internal organisational labels have been
> replaced with bracketed placeholders
> such as `[private-workspace]` and `[unrelated-work]`. No word of the review's
> substance — no finding, quotation, number, ruling or adjudication — was
> altered, added or removed.

---

**RULING: CONDITIONAL.** Four conditions, all one-line edits, none of them
touching a theorem, a proof or a load-bearing constant.

The repair round is of high quality. **All six blocking findings (F1–F6) landed,
faithfully, with no softening and no overcorrection**, and three of them (F3, F5,
F11) genuinely leave the paper stronger than R1 found it. **All three of the
repair agent's deviations from my predecessor's drafted repairs are adjudicated
SOUND** — and on deviation 2 the repair agent is right and my predecessor was
wrong, by a factor of 14 at $N=1292$. The three engines re-run here at
**43 / 6 / 4 PASS, exit 0**, and the new K4–K5 rational-interval checks are a real
second engine, not a re-skin of the first.

What holds the ruling short of PROMOTE is that the round reintroduced, in two
places, exactly the defect class F13/F14 were about — **the paper saying something
false about its own arithmetic and its own engines** — plus one printed constant
that is wrong in its fifth significant figure and that my predecessor wrongly
certified as correct. Details at N-1 … N-4.

---

## 0. Freeze check — PASSED

```
$ git log --oneline -1 -- [private-workspace]/k5-paper/
b0503151 K5 paper REPAIR ROUND R1: 26/26 executed, 0 dissents; ...
$ git status --porcelain [private-workspace]/k5-paper/
(empty)
```

`b0503151` is the last commit touching the directory and the directory is clean.
(The working tree carries unrelated dirt under `[unrelated-work]`;
nothing under `k5-paper/`.) State is as frozen. No git
beyond this read-only check; the paper was not edited.

## 0.1 Engines, re-run on this machine

| engine | exit | assertions | wall |
|---|---|---:|---|
| `verify_dimension_law.py` | **0** | **43** PASS / 0 FAIL | ~1 s |
| `verify_krs_dimension.py` | **0** | **6** PASS / 0 FAIL | ~16 s |
| `verify_transport_dimension.py` | **0** | **4** PASS / 0 FAIL | ~2 s |

43 / 6 / 4 and exit 0 confirmed, as the repair log reports.

## 0.2 My own instrument (shares no method with either engine)

Every number adjudicated below was re-derived in a referee's script that uses
**neither** engine's method: $\sqrt5$ is obtained as a two-sided *rational* bound
from `math.isqrt(5·10^{400})`, fourth roots by bisection on `Fraction`s to 80
digits. No `Decimal`, no float in any load-bearing step, no $\mathbb Q(\sqrt5)$
class, no continued-fraction recursion in the certificate. The transport
reduction of F4 was re-implemented from the paper's prose, not from engine 3.

---

## 1. Per-finding table

| # | ruling | note |
|---|---|---|
| **F1** $\Sigma_n$ definition | **CONFIRMED FAITHFUL** | Hilbert-space set + $\Sigma_n^{\mathrm{fd}}$ installed; **all 13 downstream $\Sigma$ sites independently re-audited — no stale use.** See §2.1. |
| **F2** six-figure plateau | **CONFIRMED FAITHFUL** | $N=1292$, $1.88/7.52$ decades, at every site. C14 now has a real tolerance *and* a discrimination clause. See §2.2. |
| **F3** the $2.176$ convention crossing | **CONFIRMED FAITHFUL** | Denominator-form Theorem A re-derived line by line here and is correct; cross-convention quote gone; $10.9$–$21.8$ stated alongside. See §2.3. |
| **F4** T1 tested a third of its claim | **CONFIRMED FAITHFUL** | Re-implemented independently: **0 samples in $(2,3]$**, structurally, not by luck. See §2.4. |
| **F5** the $\varphi$ inversion | **CONFIRMED FAITHFUL** | $0.8506508 < 0.9732490$ confirmed to 10 digits; general two-parameter formula sound. *But see N-2 and R-1.* |
| **F6** §6.3's closing sentence | **CONFIRMED FAITHFUL** | Now scoped to topological/dynamical invariants; matches the Abstract; §6.4's table no longer contradicts it. |
| **F7** Shulman | **CONFIRMED FAITHFUL** | `T. Shulman`, PAMS **137** (2009) 115–122, everywhere incl. engine 3; "her Theorem 15" at both sites; primary-by-proxy added to §7.3. |
| **F8** DPP Thm 4.2 / Cor 4.4 | **CONFIRMED FAITHFUL** | Verbatim as drafted. |
| **F9** "the constant is pinned" | **SOFTENED** | Abstract and §5.2 repaired correctly; **§1.4 item 3 still says the construction "pins the constant"** — the one surviving site. Condition **N-3**. |
| **F10** "everything else is an identity" | **CONFIRMED FAITHFUL** | $1.0574$ and $2.058$ both re-derived independently ($1.057371$, $2.0581$). |
| **F11** universal quantifiers | **CONFIRMED FAITHFUL** | Option (a) taken; both proofs checked line by line and both are correct. Deviation 3 adjudicated SOUND. See §3.3. |
| **F12** §7.1 whipsaw + self-citation | **CONFIRMED FAITHFUL** | Hedges gone; Disclosure paragraph present; the $14\%$ first-rate gap now in the text; DOIs reconciled. |
| **F13** verification-stack claims | **CONFIRMED FAITHFUL** | All three replaced with true statements; engine 3's `BETA` float **deleted** (verified: no float, no `Decimal`, no $\sqrt5$ anywhere in engines 2–3). *Minor overstatement at R-4.* |
| **F14** drafting note + Remark 3.6 | **CONFIRMED FAITHFUL** | Audit-of-the-rendering block is honest and names the false version as false; **C5b is a genuine fixture** — marginals $0.4622954 \neq 0.3868863$, mean exactly $t_\ast$, deficit $=(\tfrac52-\sqrt5)(\sqrt5-\tfrac43)$ asserted exactly. |
| **F15** paraphrase in quotes | **CONFIRMED FAITHFUL** | Full DPP sentence quoted; §1.2 block quote untouched. |
| **F16** Coladangelo–Stark | **CONFIRMED FAITHFUL** | `[CS20]` added and cited; arXiv:1904.02350 acknowledged. |
| **F17** [Kru02] translation | **CONFIRMED FAITHFUL** | Ukrainian Math. J. **54** (2002) 967–978; translation's title adopted; variant renderings noted. |
| **F18** infimum vs lower bound | **CONFIRMED FAITHFUL** | Referee's sentence installed in §2.4. |
| **F19** total-dimension convention | **CONFIRMED FAITHFUL** | Third row correct — $9.732$–$19.46$, $41.2$–$82.4$, $21.8$–$43.5$ all re-derived. *Residual R-5.* |
| **F20** §2.2 structural claim | **CONFIRMED FAITHFUL** | Organising-observation label + "none is used below". |
| **F21** "attained" | **CONFIRMED FAITHFUL** | All three sites. |
| **F22** three objects called $q$ | **CONFIRMED FAITHFUL** | $\kappa$ in §2.2 and in the engine (`kappa = 0.1458980338`). |
| **F23** five statement slips | **CONFIRMED FAITHFUL** | All five; `>` in Theorem A, "least *block* dimension", $\bigoplus_5 M_3\subset M_{15}$, box convention named, $20.6$–$41.2$ cell filled. |
| **F24** three empty checks | **CONFIRMED FAITHFUL** | C1 now really tests the max-of-three-branches claim on a 121-point exact grid; C8's dead `worst`/`five_q2` block deleted; C20 tests the label's own conclusion with both truth values occurring; C10 gained the substantive $\inf<\liminf$ assertion at $q=4$. |
| **F25** $5\nmid p$ | **CONFIRMED FAITHFUL** | The mod-5 pair map $(a,b)\mapsto(b,a-b)$ from $(2,4)$ is 4-periodic — verified; residues $2,4,3,1$ never $0$; asserted in C14 over 62 terms *and* the periodicity. |
| **F26** citing-set sweep | **CONFIRMED FAITHFUL** *(honest substitution)* | R1's drafted repair (name API/query/date) was **unexecutable** — the metadata does not exist. Downgrading the claim from "check" to "supporting evidence, not reproducible", in place, is the only honest move and fully answers R1's objection ("cannot be reproduced or defended"). Not a softening. |

**Totals: 24 CONFIRMED FAITHFUL, 1 CONFIRMED FAITHFUL (honest substitution),
1 SOFTENED, 0 OVERCORRECTED, 0 MISSING.**

---

## 2. The priority checks, in detail

### 2.1 F1 — the $\Sigma_n$ audit, done independently

I enumerated every occurrence of $\Sigma$ in the paper (13 sites, lines 229, 258,
260, 266–283, 289/293, 310/312, 729, 897–898, 948, 1069, 1078, 1212, 1244) and
classified each against the corrected definition. **No stale use survives.** The
one site R1 flagged for edit (§6.2's "point of the discrete part of $\Sigma_5$")
now correctly routes $4/3$ through $\Sigma_5^{\mathrm{fd}}$ via Prop. 6.1's own
construction. Lemma 4.7's "irreducible $p/q\in\Sigma_n$" and §5.4's
"$\varphi$ lies in $W$" are *more* correct under the new definition than under the
old one — $\varphi$ is irrational, so it is in $\Sigma_5\setminus\Sigma_5^{\mathrm{fd}}$,
and the paper nowhere claims a finite-dimensional realisation for it. §2.1's own
guardrail sentence ("every dimension statement in this paper is about
$\Sigma_n^{\mathrm{fd}}$") is true.

### 2.2 F2 — the honest plateau, and whether C14 now tests it

Every site carries the honest claim: Abstract (l. 95–96), Thm 1.1(B) (l. 206–209),
Thm B (l. 564–565), §4.2 (l. 582–593), drafting note (l. 51–56), Table 8.1
(l. 1165). No "from $N=17$" survives anywhere as a flatness claim.

C14 is now three assertions where it was one:
`< 5e-3` on the $N\ge17$ tail, `< 5e-7` on the $N\ge1292$ tail, **and**
`any(|r-ASY| >= 5e-7 for N < 1292)` — a discrimination clause, so the check fails
if the plateau ever starts earlier than the sentence says. All comparisons are in
80-digit `Decimal`. **The engine now certifies the sentence the paper prints.**
K5 reproduces the same three facts by a disjoint route.

Decade spans re-derived: $\log_{10}(98209/1292)=1.8809$ → **1.88**;
$\log_{10}(3.2199{\times}10^{-13}/9.6447{\times}10^{-21})=7.5237$ → **7.52**;
and the table spans $3.7618$ → **3.76**, $15.048$ → **15.05**. All correct.

### 2.3 F3 — is the denominator statement proved *as stated*?

Yes. I re-derived Theorem A's chain independently:

* $s_l=a_l/n_l$ with $a_l\in\mathbb Z$, so writing $s_l=p_l/q_l$ in lowest terms
  gives $q_l\mid n_l$, hence $Q=\max_l q_l\le\max_l n_l=N$. ✓
* $|s_l-\sqrt5| = |p_l-q_l\sqrt5|/q_l \ge \lVert q_l\sqrt5\rVert/q_l > 1/(5q_l^2)
  \ge 1/(5Q^2)$ — Lemma 3.3 applied at $q_l$, which is legitimate because
  Lemma 3.3 quantifies over *all* integers $q\ge1$. ✓
* $\varepsilon\ge\sum_l\lambda_l(s_l-\sqrt5)^2 > 1/(25Q^4)$ since
  $\sum_l\lambda_l=1$. ✓
* $\varepsilon>1/(25Q^4)\iff Q\varepsilon^{1/4}>25^{-1/4}$, and for a carrier of
  deficit $\delta\le\varepsilon$, $Q>0.4472\,\delta^{-1/4}\ge0.4472\,\varepsilon^{-1/4}$.
  So "$D(\varepsilon)>0.4472\,\varepsilon^{-1/4}$ in the denominator convention"
  is exactly right, and the "a fortiori in actual block dimension" follows. ✓

The two conventions now genuinely meet: in Theorem B's two-block carrier the
block value $s_l$ *is* $\lambda_l$, whose denominator is the $N$ of the §4.2
table. So $0.9732489895/0.4472135955$ is a within-convention ratio. Independently:
$= 2.176250$. The convention-crossed quote is gone from §4.2, Remark 3.5, the
Abstract, §5.1 and Table 8.1; §4.2 adds "the two numbers must not be crossed" and
C15 gained a second assertion pinning $10.88$–$21.76$. §5.1's old
"$\ge0.2236$ via Lemma 4.6" is gone and the lower bound no longer touches
Lemma 4.6. **F3 is not merely repaired; it is the strongest thing this round
produced.** C9b tests the reduced-denominator step on deliberately non-reduced
block data ($6/4$, $30/20$, $306/136$, …) with a `strict_gain` flag ensuring at
least one fixture has $q_l<n_l$ — a real test, not a fixture that passes vacuously.

### 2.4 F4 — re-run, and re-implemented from scratch

Engine 3 re-run here: `{0: 869, 1: 2878, 2: 218, 3: 29, 4: 6}`, sums to 4000,
max 4 steps, **0 samples in $(2,3]$**, `d=2q` recovered 4000/4000.

I then re-implemented the reduction from the paper's prose (my own sample of 4000
in-window rationals, Tits-form membership test, my own pull-back):

```
step histogram : {0: 853, 1: 2909, 2: 197, 3: 34, 4: 6, 5: 1}
landed in (2,3] (unproved region) : 0
round-trip d = 2q recovered : 4000 / 4000
--- the OLD loop on the SAME sample:  {0: 2665, 1: 1097, ...},  1812 in (2,3]
```

Two things this establishes that the engine alone does not. First, **0 in $(2,3]$
is structural, not sample luck** — the `while not (3/2 <= a <= 2)` loop cannot
exit anywhere else. Second, the old loop's pathology reproduces on a *different*
sample (1812/4000 vs R1's 1821/4000), confirming R1's diagnosis was about the
algorithm and not about `seed(7)`.

T1's assertions are real, including the non-circularity one
(`zero_step == sum(1 for a0 in sample if in_base(a0))`). `landed_seed` is
reported, not asserted — the right design, since Lemma 4.6(c) covers the seeds.

### 2.5 F5 — the $\varphi$ comparison

Independently, to 10 digits: $(\varphi/\sqrt5)^{1/2}=0.8506508083$,
$((2{+}\sqrt5)/(2\sqrt5))^{1/2}=0.9732489894$, ratio $0.874032$. Floors
$20^{-1/4}=0.47287080$, $5^{-1/4}=0.66874030$, ratio $1.41421356=\sqrt2$ — not 2.
**$\varphi$ is cheaper, and the two ends move in opposite directions.** The
general formula
$N\varepsilon^{1/4}\to(\rho/(\alpha-\alpha'))^{1/2}$ is sound: it is Prop. 4.1's
product identity plus $|h_n/k_n-\alpha|\sim1/((\alpha-\alpha')k_n^2)$, and C26
recomputes both constants *from the construction*, not from the formula — the
right design. "twice as hard" and "$\sqrt5$ is a factor 2 cheaper" are gone; the
liminf ratio 2 survives, correctly rescoped in C25 with a pointer to C26.

### 2.6 F13/F14 — is the stack description literally true?

Verified by reading the shipped engines, not the log.

* Engines 2 and 3 contain **no** `float`, **no** `Decimal`, **no** `math.sqrt`,
  **no** `**0.5`, no $\mathbb Q(\sqrt5)$ or $\mathbb Q(\zeta_5)$ class — only
  `fractions.Fraction` and integers. Engine 3's `BETA = (5-5**0.5)/2` is gone;
  window membership is `p*p - 5*p*q + 5*q*q <= 0`. ✓
* Engine 3's docstring and §8 both state the sequential dependence on engine 2. ✓
* §8's "not every numbered claim" list matches Table 8.1's six *not checked* rows,
  and Remark 3.6 now points at C5b rather than the fixture that could not support
  it. ✓

**K4–K5 are a genuine second engine.** The bracket for $\sqrt5$ is certified by
`lo*lo < 5 < hi*hi` (integer comparison, ~76-digit denominators, width
$<10^{-149}$), not by any theory; `eps_bracket` **asserts** $\lambda_1>hi$,
$\lambda_2<lo$ and that the concave vertex $(\lambda_1{+}\lambda_2)/2$ lies
outside $[lo,hi]$ so the endpoint evaluation really does bracket $\varepsilon$
(so straddling is independently certified too); and `rel_within` reduces
$|N\varepsilon^{1/4}/A-1|<t$ to $(1-t)^4 X^2_{hi} < N^4\varepsilon_{lo}$ and
$N^4\varepsilon_{hi} < (1+t)^4 X^2_{lo}$ — sound in both directions, and a pure
integer/rational comparison. Nothing in K4–K5 shares an algorithm or a number
representation with engine 1's $\mathbb Q(\sqrt5)$-plus-`Decimal`-fourth-root
route. The paper's sentence claims exactly what K4–K5 establish — the §4.2 table
and Theorem B's two tolerances — and no more. *One overstatement remains: R-4.*

---

## 3. Adjudication of the three deviations

### 3.1 Deviation 1 — rejecting "monotonically convergent". **SOUND.**

The repair agent refused my predecessor's word and was right to. Independently,
the sign of $N\varepsilon^{1/4}-A$ down the table:

```
N =  2 ABOVE,  4 below, 17 ABOVE, 72 below, 305 ABOVE,
  1292 below, 5473 ABOVE, 23184 below, 98209 ABOVE
```

Perfect alternation at every rung — the sequence oscillates about its limit and is
monotone on no tail. (What *is* monotone is $|N\varepsilon^{1/4}-A|$; a reader
could charitably have meant that, but "monotonically convergent" applied to a
sequence asserts the sequence is monotone, and it is not.) Implementing my
predecessor's word verbatim would have installed a new false claim in the
Abstract. The paper says "computed across" and "convergent", which is true.
**Deviation upheld; the referee's draft was wrong here.**

### 3.2 Deviation 2 — correcting my predecessor's deviation figures. **SOUND, and the repair agent's numbers are the correct ones.**

The caller asks for an independent adjudication between `2.81e-6 / 1.57e-7`,
`3.1e-6 / 1.1e-8`, and "neither". Re-derived with `isqrt`-based rational bounds
and bisection fourth roots, sharing no code with either engine:

| $N$ | $N\varepsilon^{1/4}$ | relative deviation (this referee) | R1 verdict said | repair log says |
|---:|---|---|---|---|
| 17 | 0.974132520 | $9.078\times10^{-4}$ | $9.1\times10^{-4}$ ✓ | (unchanged) ✓ |
| 72 | 0.973199844 | $5.050\times10^{-5}$ | $5.0\times10^{-5}$ ✓ | (unchanged) ✓ |
| **305** | 0.973251728 | $\mathbf{2.8144\times10^{-6}}$ | $3.1\times10^{-6}$ ✗ | $2.81\times10^{-6}$ **✓** |
| **1292** | 0.973248836 | $\mathbf{1.5684\times10^{-7}}$ | $1.1\times10^{-8}$ ✗ | $1.57\times10^{-7}$ **✓** |

**The answer is $2.81\times10^{-6}$ and $1.57\times10^{-7}$.** My predecessor was
wrong at both rungs, and at $N=1292$ wrong by a factor of $14$ — an error that,
had it stood, would have made the plateau look an order of magnitude tighter than
it is. The repair agent caught it, corrected it against two engines, and — this is
the part that matters — **checked that the finding's conclusion survives the
correction**, which it does: $1.57\times10^{-7}$ is still inside six significant
figures ($<5\times10^{-7}$) and $2.81\times10^{-6}$ is still outside. The tail
figures the paper adds ($8.7\times10^{-9}$, $4.9\times10^{-10}$,
$2.7\times10^{-11}$) also reproduce ($8.740$, $4.871$, $2.714$). **Deviation
upheld; this is the round's best catch, and it is a catch on the referee.**

### 3.3 Deviation 3 — the new termination proofs. **SOUND. Both proofs are correct.**

These are new mathematics written during repair, so I checked every line.

**Lemma 4.5.** First, the diagnosis. My predecessor proposed that the decrease of
$3l-m-\sum_{i\le j}k_i$ by $k_j\ge1$ "so the recursion terminates in
$\le 3l-m-1$ steps" closes it. The repair agent is right that this does not close:
the recursion runs a *prescribed* $s=m-l$ steps, and what the dimension count
needs is the exact identity $\sum_j k_j = 3l-m-1$, which a monotone-decrease
budget cannot deliver. **The referee's sketch was a budget bound, not a proof.**

The replacement, verified step by step:

* *(i) Legality.* $k_j$ is characterised by $0<r_j\le\epsilon$, i.e.
  $k_j<u_j/\epsilon\le k_j+1$, i.e. $k_j=\lceil u_j/\epsilon\rceil-1$ — correct,
  including the integer edge case. Base: $u_1=3-\alpha=2-\epsilon$. ✓ Step: from
  $u_j\in[2-\epsilon,2]$, $u_j/\epsilon\in[2/\epsilon-1,\,2/\epsilon]$, and
  $\epsilon<1\Rightarrow 2/\epsilon-1>1$, $\epsilon>\tfrac12\Rightarrow 2/\epsilon<4$,
  so $u_j/\epsilon\in(1,4)$ and $k_j\in\{1,2,3\}$, uniquely. ✓ Then
  $b_{j+1}=\alpha-r_j\in[1,\alpha)$ and $u_{j+1}\in(2-\epsilon,2]\subset[2-\epsilon,2]$,
  closing the induction. ✓ This is exactly [KRS02, Prop. 5]'s hypothesis
  $1\le b\le\alpha$. ✓ **Both strict inequalities $\tfrac12<\epsilon<1$ are used,
  which is precisely why the lemma is stated on the open interval $(3/2,2)$** — and
  Lemma 4.6(c) handles the two closed endpoints separately. Consistent.
* *(ii) Termination.* $r_j\equiv u_j \pmod\epsilon$; $u_{j+1}=3-\alpha+r_j=(2-\epsilon)+r_j\equiv2+r_j$;
  induction from $r_1\equiv2$ gives $r_j\equiv2j$. At $j=s$, $2s=2l\cdot\epsilon\in\epsilon\mathbb Z$
  because $\epsilon=s/l$ and $2l\in\mathbb Z$, so $r_s\equiv0$; with
  $r_s\in(0,\epsilon]$ this forces $r_s=\epsilon$. ✓ **Correct, and the parenthetical
  identifying this as where the base interval enters is right.**
* *(iii) Dimension.* $b_{j+1}=b_j+(k_j+1)\epsilon-2$ ✓ (algebra checks).
  Telescoping with $b_{s+1}=\alpha-\epsilon=1$ gives $(\sum k_j+s)\epsilon=2s-\epsilon$,
  hence $\sum k_j+s=2s/\epsilon-1=2l-1$ and $\sum k_j=3l-m-1$. ✓
  $\dim=\sum(k_j+2)-(s-1)=\sum k_j+s+1=2l$. ✓ Matches K1–K3's exhaustive output
  on all 7921 cases.

No lowest-terms hypothesis is needed anywhere in the proof, which is right —
K1 tests non-reduced $m/l$ too (4915 of 7921 are reduced). One clarity residual at
R-2.

**Lemma 4.6.** (a) $\Phi^-(p/q)=(4p-5q)/(p-q)$ with
$\gcd(4p-5q,p-q)\mid 4(p-q)-(4p-5q)=q$ and hence $\mid\gcd(q,p)=1$ ✓;
$2q\mapsto((p-q)/q)2q=2(p-q)$ ✓. $\Phi^+(p/q)=(5q-p)/(4q-p)$, common divisor
divides the difference $q$ ✓, $2q\mapsto2(4q-p)$ ✓. $T(p/q)=(5q-p)/q$,
$\gcd(5q-p,q)=\gcd(p,q)=1$ ✓, $d$ and denominator both fixed ✓.
(b) $\alpha>3\Rightarrow T\alpha\in(\lambda_-,2)$ ✓ (no rational equals
$\lambda_+$); $\alpha\in(2,3]\Rightarrow 4-\alpha\in[1,2)\Rightarrow\Phi^+\alpha\in(3/2,2]$ ✓;
$\Phi^-$ is increasing with $\Phi^-(\lambda_-)=\lambda_-$, $\Phi^-(3/2)=2$, so it
maps $(\lambda_-,3/2)$ into $(\lambda_-,2)$ ✓, while $p<\tfrac32q\Rightarrow p-q<q/2$
so denominators at least halve — halting in $\le\log_2 q$ steps ✓. The four cases
$(\lambda_-,3/2)$, $[3/2,2]$, $(2,3]$, $(3,\lambda_+)$ exhaust $W$. ✓
(c) The two seeds are exhibited and doubled to make the bookkeeping exact at
$d=2\times$denominator ✓.

**Both proofs are correct.** Two residuals, neither an error: R-2 and R-3.

---

## 4. New findings (this round)

### N-1 — CONDITION. The uniform constant is $4.1227$, not $4.1226$; the check's tolerance is too loose to see it, and the engine prints the right value one line below the wrong one.

$$0.9732489894677302\times(2+\sqrt5)\;=\;\mathbf{4.12274887841828\ldots}$$

re-derived here to 20 digits. The paper prints:

* §5.2, l. 791: "$0.9732489895\times(2+\sqrt5)\;=\;4.1226\ldots$" — the ellipsis
  asserts the digits, and the digits are $4.12274\ldots$;
* Table 8.1, l. 1172: "uniform constant $4.1226$".

C16 asserts `abs(ASY*(2+5**0.5) - 4.1226) < 1e-3`, and $|4.122749-4.1226|=1.5\times10^{-4}$
passes — **the check's tolerance is 7× too loose to discriminate**, which is the
same defect class as the pre-repair C14. Worse, C16's own detail field prints
`uniform constant 4.1227` immediately after its label prints `= 4.1226`, so the
engine contradicts itself inside one line of output.

§5.1's cell ($4.123$) and the drafting note's source statement ($4.123$) are
**correct** — only the four-decimal renderings are wrong. Note also that
§5.1's derived cells are right ($5\times4.12275=20.61$, $10\times=41.23$), so
nothing downstream moves.

*This is also a miss by my predecessor*, who listed "the uniform constant
$4.1226$" in the R1 "what is not wrong, and should not be touched" section. It was
wrong then and it is wrong now. **Fix: $4.1227$ at both sites; tighten C16 to
`< 1e-4` against `4.1227`.**

### N-2 — CONDITION. §5.4 misdescribes check C26 — the F13/F14 defect class, reintroduced by the F5 repair.

Paper, l. 847–848: "All four constants are check C26 (recomputed in $60$-digit
`Decimal` over $30$ convergents of each)."

Shipped C26: `getcontext().prec = 140`, **40** convergents of $\sqrt5$ and **90**
of $\varphi$. The repair log itself says "40 convergents of $\sqrt5$ and 90 of
$\varphi$ in 140-digit `Decimal`", and the check's own printed label says
"40 resp. 90 convergents in 140-digit Decimal". So the paper contradicts both the
log and the engine. (A stale comment at engine l. 1020–1021 says "30 convergents …
60+ digit", which is presumably where the paper's sentence came from.)

The direction is harmless — the paper *understates* its own verification — but
F13 and F14 were findings about precisely this: the paper asserting things about
its engines that are not true of the shipped files. **Fix: "recomputed in
140-digit `Decimal` over 40 and 90 convergents respectively"; update the engine
comment.**

### N-3 — CONDITION. F9 has a surviving site: §1.4 still says the construction "pins the constant".

Paper, l. 241–244 ("New here", item 3): "…together with the convergent
construction that makes the exponent tight **and pins the constant**."

F9's finding was that the constant of $D$ is *bracketed*, not pinned, because $D$
is a minimum over all carriers. The Abstract and §5.2 were repaired correctly and
§5.2 now says explicitly "Neither is claimed to be the constant of $D$ itself".
§1.4 was not swept, and it is in the paper's four-item claim of novelty — the most
quotable list in the document. **Fix: "…and fixes the constant along that family"
or "…and exhibits the sharpest attained constant".**

### N-4 — CONDITION (engine hygiene). Engine 1's C14 comment still carries my predecessor's *incorrect* deviations, which Deviation 2 corrected.

`verify_dimension_law.py`, l. 729–731:

```python
#        figures from N = 17" was FALSE (repair round R1, finding F2): the
#        relative deviations at N = 17, 72, 305 are 9.1e-4, 5.0e-5, 3.1e-6.
#        Six figures begin at N = 1292 (relative deviation 1.1e-8).
```

`3.1e-6` and `1.1e-8` are the two figures the repair round *corrected* and the
paper no longer prints. The same file, twenty lines later, prints
`N=305: 2.81e-06, N=1292: 1.57e-07`. A shipped appendix that states the wrong
number in a comment and the right number in its output is exactly what a hostile
reader screenshots. **Fix: two numbers in a comment.**

### Residuals (recorded, not conditions)

* **R-1.** §5.4's displayed floor $N\varepsilon^{1/4}>(\liminf_q q\lVert q\alpha\rVert)^{1/2}$
  drops the qualifier that §3.3 declares load-bearing. §3.3 proves
  $\inf_q q\lVert q\sqrt5\rVert = 0.2229124 < 1/\sqrt{20}$ at $q=4$ and says in
  terms that "the word 'asymptotic' is load-bearing and cannot be dropped"; §5.4
  then writes the liminf constant into a strict inequality with no qualifier, and
  the table's $\sqrt5$ floor cell reads $0.4729$ where Theorem A's proved floor is
  $0.4472$. Mitigated — but only just — by §5.4's closing sentence scoping the
  whole display as "the shape of the general answer, not a theorem". One word
  ("asymptotically") in the display would close it.
* **R-2.** Lemma 4.5(ii) proves $r_s=\epsilon$ but does not remark that
  $r_j=\epsilon$ also occurs at $j=s/2$ whenever $s$ is even (there
  $2j\equiv0\bmod\epsilon$ too). This is harmless — $b_{j+1}=1$ is legal and the
  block count is prescribed, not a stopping time — but the lemma's word
  "terminates after $s=m-l$ blocks" reads as a derived stopping time. One
  clause would prevent a referee raising it.
* **R-3.** Lemma 4.6(c)'s pull-back proves the *dimension bookkeeping* is exact
  and cites [KRS02, eq. (2.5)] for the functors; it does not argue that the
  inverse Coxeter functor delivers a genuine representation rather than
  degenerating. This is incumbent machinery the paper explicitly labels recovery
  (§1.4), and positivity of the dimension vector is maintained throughout, so I do
  not treat it as a gap — but it is the one place where the proof leans on cited
  functor theory without saying so.
* **R-4.** §8's "two engines that share neither an algorithm nor a number
  representation" is a shade strong: both engines generate the $\lambda$ pairs
  by the same recursion $h\leftarrow4h+h'$. The pairs are *inputs* to the claim
  and engine 2 independently certifies that they straddle its verified bracket,
  so nothing is circular — but "share no number representation and no evaluation
  algorithm" would be exactly true.
* **R-5.** §5.1's new total-Hilbert-dimension row (the F19 repair) has no row in
  Table 8.1, neither as checked nor in §8's *not checked* list. Its arithmetic is
  a doubling of Cor. 4.8 and I verified it, but the table's own completeness
  claim now has an unlisted entry.
* **R-6.** §2.1 asserts $\Sigma_n^{\mathrm{fd}}=\Sigma_n\cap\mathbb Q$ for all
  $n\ge2$ on the authority of [KRS02, Thm. 6] plus the trace obstruction, where
  the cited theorem is about rationals *in the window* for $n\ge5$. This is my
  predecessor's own drafted wording, so the repair is faithful; the
  over-generalisation is inherited, not introduced.
* **R-7.** §4.3's "at most 4 transport steps" and "none on a seed" are properties
  of `seed(7)`, not of the reduction: my resample produced a 5-step case and 21
  seed landings. Nothing is load-bearing on either — Lemma 4.6(c) covers the
  seeds and the step count is reported, not asserted — but the phrasing reads as a
  bound.
* **R-8.** §5.4 says $\varphi$ is "$13\%$" cheaper; the computed figure is
  $12.60\%$ (ratio $0.874032$). The repair log says $12.6\%$. Legitimate rounding,
  recorded only so a later round does not re-open it.

---

## 5. Spot-checks of paper numbers (independent instrument)

| paper number | site | this referee | verdict |
|---|---|---|---|
| $\varepsilon(5/2,2)=(9\sqrt5-20)/2=6.2306\times10^{-2}$ | §4.2, C18 | $0.062305898749$, and $(9\sqrt5-20)/2$ agrees to 12 dp | ✓ |
| $\varepsilon(9/4,38/17)=(305\sqrt5-682)/68$ | §4.2, C18 | $1.0781432880\times10^{-5}$, closed form agrees to 18 dp | ✓ |
| factor $5779$ | §4.2 | $5778.9995$ → $5779$ | ✓ |
| $(2+\sqrt5)^4=321.9968944$ | §5.2, C16 | $321.9968943\ldots$ | ✓ |
| $25^{-1/4}=0.4472135955$ | Thm A | $0.447213595499\ldots$ | ✓ |
| $A=0.9732489895$ | Thm B | $0.97324898946773016$ | ✓ |
| $A/25^{-1/4}=2.176$ | §4.2, §5.1 | $2.176250$ | ✓ |
| $(5/\sqrt{20})^{1/2}=1.0574$ | Rem 3.5 | $1.057371$ | ✓ |
| $A/20^{-1/4}=2.058$ | Rem 3.5 | $2.0581$ | ✓ |
| $C_{\rm act}\in[4.866,9.732]$; $10.9$–$21.8$ | Cor 4.8, §5.1 | $4.8662449$, $9.7324899$; $10.881$, $21.763$ | ✓ |
| $\varphi$ row $0.6687/0.8507$ | §5.4 | $0.66874030$, $0.8506508083$ | ✓ |
| $\lambda_-=1.381966$, $\kappa=\varphi^{-4}=0.1458980$ | §2.2 | agree | ✓ |
| $4/3$ orbit $11/8,29/21,76/55,199/144$; vectors $(40,11),(105,29),(275,76)$; $\mathfrak q\equiv+5$ | §6.2 | recomputed by hand from $M_5$; all agree | ✓ |
| $5/2$ vectors $(3,1),(7,2),(18,5),(47,13)$; $\mathfrak q(2,1)=-1$ | §6.3 | agree | ✓ |
| $h_n\bmod5=2,4,3,1$ cyclically | Lem 4.7 | $2,9,38,161,682,2889,12238,51841,219602\to2,4,3,1,2,4,3,1,2$ | ✓ |
| **uniform constant $4.1226$** | **§5.2, Table 8.1** | **$4.12274887841828$** | **✗ — N-1** |

Sixteen checks, fifteen clean. No arithmetic in the body of the paper is wrong.

---

## 6. Conditions for PROMOTE

1. **N-1** — $4.1226\to4.1227$ in §5.2 and Table 8.1; tighten C16.
2. **N-2** — §5.4's description of C26 (140-digit; 40 and 90 convergents).
3. **N-3** — §1.4 item 3: drop "pins the constant".
4. **N-4** — engine 1, l. 730–731: replace the two stale deviations.

Optionally sweep R-1 (one word) and R-4 (one clause); both are cheap and both are
in sentences a referee will read adversarially.

None of these touches a theorem, a proof, a constant of Theorem A or B, an engine
result, or any of the F1–F26 repairs. On discharge this promotes.

---

**Summary.** The repair round did what a repair round should: it executed all 26
findings, it refused the referee where the referee was wrong, and on the one
substantive disagreement — the relative deviations at $N=305$ and $N=1292$ — it
was right and the referee was wrong by a factor of 14. The two new proofs written
during repair are correct, and the F3 and F13 repairs are strict improvements to
the paper rather than retreats. What remains is four one-line defects of the same
species the round was convened to kill: a printed constant that is wrong in its
fifth figure, a sentence that misdescribes the paper's own engine, an unswept
occurrence of a word already retracted elsewhere, and a stale comment in a shipped
appendix. Fix those four and the paper is clean.

---
---

# R2b — residual confirmation

**RULING: PROMOTE.**

State re-frozen and re-verified at `a8378bbd`. `git diff --stat b0503151 a8378bbd`
over the directory shows exactly three files touched — `PAPER-K5.md` (21 lines),
`appendix/verify_dimension_law.py` (8 lines) and this verdict file — and
`git status --porcelain` on the directory is empty. Nothing outside the four
conditions and the two recorded observations moved. The paper was not edited by
me; this section is an append.

## Engines, re-run at `a8378bbd`

| engine | exit | assertions |
|---|---|---|
| `verify_dimension_law.py` | **0** | **43** PASS / 0 FAIL |
| `verify_krs_dimension.py` | **0** | **6** PASS / 0 FAIL |
| `verify_transport_dimension.py` | **0** | **4** PASS / 0 FAIL |

## Condition-by-condition

### N-1 — the uniform constant. **DISCHARGED.**

Recomputed here from scratch (`isqrt`-based rational bounds on $\sqrt5$ to 300
digits, bisection square root, no `Decimal` and no float):

$$0.9732489894677301637880\times4.2360679774997896964091
=\mathbf{4.1227488784182818386761\ldots}$$

The coordinator asks specifically whether $4.12275$ is "the right truncation". It
is not — it is the right **rounding**. To six significant figures the truncation
is $4.12274$ and the rounding is $4.12275$. That distinction is worth stating,
because it was the basis of my N-1 objection; the objection nonetheless stands
discharged, for two reasons:

1. **$4.1226$ was wrong under *every* reading** — neither the truncation
   ($4.12274$) nor the rounding ($4.12275$), and off by $1.5\times10^{-4}$, i.e.
   wrong in the fifth significant figure. $4.12275$ is exact under one standard
   reading and wrong by one unit in the last place under the other. That is a
   categorical improvement, not a lateral move.
2. **It matches the paper's own established convention.** The paper already writes
   "$(2+\sqrt5)^4=321.9968944\ldots$" where the value is $321.996894379984$
   (truncation $321.9968943$, rounding $321.9968944$), and "$0.9732489895$" where
   $A=0.9732489894677\ldots$ (truncation $\ldots894$, rounding $\ldots895$). The
   paper rounds to the displayed digit and appends the ellipsis, consistently.
   $4.12275\ldots$ is that same convention correctly applied; singling it out
   would be inconsistent with leaving the other two alone, and all three are
   standard.

Downstream consistency re-checked: §5.1's cell $4.123$ ✓ ($4.122749\to4.123$),
the drafting note's source statement $4.123$ ✓, "in actual dimension $5\times$
that" against §5.1's $20.6$ ✓ ($5\times4.122749=20.6137$) and row 3's $41.2$ ✓.
No surviving $4.1226$ anywhere in `PAPER-K5.md` or in any engine — the string now
appears only in the R1 log and in the two verdicts, where it belongs as the record
of the defect.

### N-1 (b) — does C16 now actually fail on $4.1226$? **YES — verified by mutation.**

Analytically the margins are $|4.12274888-4.12275|=1.12\times10^{-6}$ (passes
$5\times10^{-5}$ with a factor-44 margin) and
$|4.12274888-4.1226|=1.49\times10^{-4}$ (exceeds it by a factor of 3). I did not
stop at the arithmetic. I copied the engine, reverted **only** the target
constant to $4.1226$ leaving the new $5\times10^{-5}$ tolerance in place, and ran
it:

```
MUTANT EXIT=1
[FAIL] C16  ... 0.9732 * (2+sqrt5) = 4.12275
FAILED: C16 ...
VERDICT: 1 check(s) FAILED
```

**The check now discriminates the value it is supposed to certify**, and the
engine exits non-zero on the old wrong constant. This is the property the
pre-repair C16 lacked: it is no longer a check that passes a statement the paper
does not make.

### N-2 — the C26 description. **DISCHARGED.**

§5.4 now reads "recomputed in $140$-digit `Decimal` over $40$ ($\sqrt5$) and $90$
($\varphi$) convergents". Checked against the shipped code: `getcontext().prec =
140`; `h5`/`kk5` built over 40 iterations; `hphi, kphi = fb[2:93], fb[1:92]`
giving 90 consecutive pairs. The sentence is now literally true of the file, and
agrees with C26's own printed label and with the repair log.

### N-3 — "pins the constant". **DISCHARGED.**

§1.4 item 3 now reads "…makes the exponent tight and **brackets** the constant (to
the factor $2.176$ of §4.2, in the denominator convention; it is a bracket, not a
pin)". Consistent with the Abstract ("bracketed to a factor $2.176$"), with §5.2
("Neither is claimed to be the constant of $D$ itself") and with §5.1's table. The
word "pinned" now survives in the paper at exactly one site, l. 1078 — "[Ehr00]'s
content is pinned by two primary sources" — an unrelated and correct use.

### N-4 — the stale C14 comment. **DISCHARGED.**

`verify_dimension_law.py` l. 730–731 now carries $2.81\times10^{-6}$ and
$1.57\times10^{-7}$, matching the engine's own printed output
(`N=305: 2.81e-06, N=1292: 1.57e-07`), the paper's §4.2, and my independent
re-derivation. The file no longer contradicts itself.

### R-1 — the asymptotic qualifier. **DISCHARGED.**

The §5.4 display now carries `\text{asymptotically (§3.3)}` attached to the
*first* inequality only — correct placement, since the second relation is a limit
and needs no such qualifier — and the table column is now "asymptotic floor
$(\cdot)^{1/2}$". The $\sqrt5$ floor cell $0.4729$ is now unambiguously labelled
as the asymptotic constant rather than as Theorem A's proved $0.4472$, which is
what §3.3 spends a paragraph insisting on. §5.4's closing scope sentence ("stated
as the shape of the general answer, not as a theorem") is intact.

### R-4 — the two-engine sentence. **DISCHARGED; it states no more than K4–K5 establish.**

New text: "…certified by two engines sharing no number representation and no
verification code; the one shared ingredient is the convergent recursion that
generates the $\lambda$ pairs themselves."

Audited clause by clause against the shipped files:

* *"no number representation"* — engine 1 uses $\mathbb Q(\sqrt5)$,
  $\mathbb Q(\zeta_5)$ and 80/140-digit `Decimal`; engine 2 uses
  `fractions.Fraction` and integers only. Verified: no `Decimal`, no float, no
  `math.sqrt`, no `**0.5` anywhere in engine 2's code. True.
* *"no verification code"* — the two are separate stdlib-only scripts with no
  imports between them; K4–K5's bracket-and-compare-fourth-powers route shares no
  routine with engine 1's exact-$\mathbb Q(\sqrt5)$-then-`Decimal`-fourth-root
  route. True.
* *"the one shared ingredient is the convergent recursion"* — exactly the caveat I
  raised, and correctly identified: both regenerate the $\lambda$ pairs by
  $h\leftarrow4h+h'$. True, and it is now disclosed rather than papered over.

The sentence claims no more than K4–K5 deliver: the scope is still "the §4.2 table
and the six-figure plateau of Theorem B", which is precisely what K4 (all nine
rows) and K5 (both tolerances plus the $N=305$ discrimination) certify. Note that
the $\lambda$ pairs are *inputs* to the claim and that engine 2 independently
certifies they straddle its own integer-verified bracket (`eps_bracket` asserts
$\lambda_1>hi$ and $\lambda_2<lo$), so the shared recursion introduces no
circularity — it selects which rows to check, not what the answer is.

## New decay from these ten edits: none

I re-read every edited region in context and swept the numbers each edit touches.
No claim was weakened, no cross-reference broken, no internal contradiction
created. Two nano-notes, neither a defect and neither worth an edit round:

* C16's detail field still formats the value as `4.1227` (`:.4f`) beside a label
  reading `4.12275`. Unlike the pre-repair situation — where label and detail were
  *different numbers* — these are the same number at two precisions. `:.5f` would
  be tidier.
* §1.4's "the convergent construction that … brackets the constant" credits the
  construction with a bracket whose lower end is Theorem A's, not the
  construction's. Strictly better than "pins", and the parenthetical routes the
  reader to §4.2 where both ends are named; recorded only so a later round does
  not re-open it.

## Ruling

All four conditions discharged, both recorded observations discharged, engines
43 / 6 / 4 at exit 0, and the one check whose looseness I criticised now
demonstrably fails on the value it previously waved through. Carried forward from
R2 and unchanged: 24 of 26 findings CONFIRMED FAITHFUL, one honest substitution
(F26), one softening now closed (F9), zero MISSING, zero OVERCORRECTED, and all
three repair-round deviations adjudicated SOUND — including the correction of my
predecessor's relative deviations, where the repair agent was right and the
referee was wrong by a factor of 14.

No arithmetic in this paper is wrong, and the paper's statements about its own
arithmetic and its own engines are now true. **PROMOTE.**
