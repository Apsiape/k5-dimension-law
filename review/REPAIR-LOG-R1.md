# REPAIR LOG — round R1, against `VERDICT-PAPER-BLIND-R1.md`

> **Redaction note, 2026-08-10.** This review document was produced inside a
> private working repository. Filesystem paths, repository-internal directory
> names, workspace locations and internal organisational labels have been
> replaced with bracketed placeholders
> such as `[private-workspace]` and `[unrelated-work]`. No word of the review's
> substance — no finding, quotation, number, ruling or adjudication — was
> altered, added or removed.

---

Date: 2026-08-10. Scope: `PAPER-K5.md` and the three engines in `appendix/`.

**Result: 26 of 26 findings repaired; 0 dissents.** Three of the referee's drafted
repairs were implemented in a *stronger or corrected* form than drafted; those are
flagged **[DEVIATION]** below with the reason, and none of them weakens the finding.

**Engines after repair** (repair-round machine, CPython, from `appendix/`):

| engine | exit | assertions | wall |
|---|---|---|---|
| `verify_dimension_law.py` | **0** | 43 PASS / 0 FAIL | 0.3 s |
| `verify_krs_dimension.py` | **0** | 6 PASS / 0 FAIL | 15.6 s |
| `verify_transport_dimension.py` | **0** | 4 PASS / 0 FAIL | 1.8 s |

**Paper numbers that changed** — none of the §4.2 table, neither constant, and no
theorem value moved. What changed is listed in §"Numbers" at the end.

---

## BLOCKING FINDINGS

### F1 — `Sigma_n` defined as the finite-dimensional set. **REPAIRED.**
*Location:* §2.1 (definition paragraph), plus downstream audit.

Replaced the definition with the Hilbert-space existence set per Shulman p. 1 /
KRS02 abstract, and introduced $\Sigma_n^{\mathrm{fd}}\subseteq\Sigma_n$ for the
matrix-realisable subset. Restated [KRS02, Thm. 6] + the trace obstruction as
$\Sigma_n^{\mathrm{fd}}=\Sigma_n\cap\mathbb Q$ (the previous phrasing was
vacuous). Added Shulman's explicit $\Sigma_4$ and $\Sigma_1=\{0,1\}$.

*Downstream re-audit of every use of $\Sigma_n$ (5 sites):*
- §1.4 recovery table, "trichotomy … $\Sigma_n\supseteq$ interval for $n\ge5$" —
  correct under the corrected definition; unchanged.
- §2.1 Ehrhardt, "$[3/2,5/2]\subset\Sigma_5$" — a Hilbert-space inclusion;
  correct; unchanged.
- §6.2, "point of the discrete part of $\Sigma_5$ … whose finite-dimensionality
  is [Shu07]" — **edited**: now says $4/3$ is rational, hence in
  $\Sigma_5^{\mathrm{fd}}$, which Prop. 6.1 exhibits directly.
- Lemma 4.7, "irreducible $p/q\in\Sigma_n$" — correct; unchanged.
- §5.4, "$\varphi$ lies in $W$" — $W\subseteq\Sigma_5$ (Hilbert-space);
  unchanged.

### F2 — "flat to six figures from N=17" is false. **REPAIRED.**
*Locations:* Abstract; Theorem 1.1(B); Theorem B; §4.2 (new paragraph); drafting
note; Table 8.1; engine 1 check C14; engine 2 check K5.

Took the referee's option (a) shape: report the full span *and* the six-figure
plateau separately. Six-figure flatness now stated as beginning at $N=1292$, with
the honest decade spans **1.88 of $N$ and 7.52 of $\varepsilon$** inside a table
spanning 3.76 and 15.05.

C14 was split into two assertions with two tolerances, exactly as the referee
asked: `< 5e-3` on the `N >= 17` tail and `< 5e-7` on the `N >= 1292` tail, plus a
third assertion that `N = 305` *fails* the tight tolerance (so the check
discriminates rather than merely passes). All comparisons moved from `float` to
80-digit `Decimal`.

**[DEVIATION 1 — the referee's word "monotonically".]** The referee's drafted
sentence read "monotonically convergent across $N=17\to98\,209$". The ratio is
**not** monotone: $0.999223,\ 0.957906,\ 0.974133,\ 0.973200,\ 0.973252,
\ 0.973249,\dots$ oscillates about the limit. The paper says "computed across" /
"convergent", not "monotonically convergent". Implementing the referee's word
verbatim would have introduced a new false claim.

**[DEVIATION 2 — two of the referee's relative deviations do not reproduce.]**
The verdict's table gives $3.1\times10^{-6}$ at $N=305$ and $1.1\times10^{-8}$ at
$N=1292$. Engine 1 (80-digit `Decimal`, exact $\mathbb Q(\sqrt5)$ deficits) gives
$2.81\times10^{-6}$ and $1.57\times10^{-7}$; engine 2's independent rational
interval re-derivation (K5) agrees. The referee's other two figures ($9.1\times
10^{-4}$ at $N=17$, $5.0\times10^{-5}$ at $N=72$) do reproduce. **The finding's
conclusion is unaffected** — $0.9732488\ldots$ still rounds to $0.973249$ at six
significant figures and $0.973252$ at $N=305$ does not — so the repair stands
exactly as drafted; only the two quoted deviations were corrected in the paper.

### F3 — cross-convention "tight to a factor 2.176". **REPAIRED** (referee's drafted improvement, in full).
*Locations:* Theorem A (restated); Remark 3.4a (new); §1.3 Theorem 1.1(A) and the
boxed statement; §4.2; §5.1 table; Abstract; Table 8.1; engine 1 checks C9b (new)
and C15 (rewritten).

Theorem A is now proved at the **reduced denominator**: writing $s_l=p_l/q_l$ in
lowest terms, $q_l\mid n_l$ and
$|s_l-\sqrt5|\ge\lVert q_l\sqrt5\rVert/q_l>1/(5q_l^2)\ge 1/(5Q^2)$, giving
$\varepsilon>1/(25Q^4)\ge1/(25N^4)$ with $Q=\max_l q_l\le N$. Consequences carried
through:
- §5.1's denominator row now reads $0.4472$ (Thm. A, directly), **not**
  $\ge0.2236$ via Lemma 4.6 — the lower bound no longer depends on Lemma 4.6 at
  all;
- §4.2 and Remark 3.5 say "tight to a factor $2.176$ **in the denominator
  convention**" and add the actual-dimension gap $10.9$–$21.8$;
- the Abstract names the convention in the same sentence;
- Theorem 1.1's box says which convention the two constants are in.

New check C9b asserts the Diophantine step at the reduced denominator on block
data whose values are deliberately non-reduced (e.g. $s=6/4$, $30/20$, $306/136$),
including $q_l\mid n_l$ and $q_l<n_l$ cases. C15 gained a second assertion pinning
the cross-convention numbers ($4.866$–$9.732$ against $0.4472$ = $10.88$–$21.76$)
so the two can no longer be confused.

### F4 — engine 3's T1 did not test what Lemma 4.6 claims. **REPAIRED** (referee's drafted engine fix).
*Location:* `appendix/verify_transport_dimension.py`, T1 loop and docstring;
Lemma 4.6's proof and its verification note in §4.3.

Transport loop now reduces into the **proved** base interval $[3/2,2]$:
`a > 3` → $T$; `2 < a <= 3` → $\Phi^+$ (one step into $(3/2,2]$); `a < 3/2` →
$\Phi^-$. Pull-back handles all three maps ($\Phi^+$: $d\mapsto(4-\alpha)d$ was
absent before). Added the referee's two assertions: landing interval is
$[3/2,2]$, and `steps >= 1` for every sample starting outside it — plus a stronger
one, that the zero-step count equals exactly the number of samples already in the
base interval.

**New step histogram (was `{0:2690, 1:1057, 2:218, 3:29, 4:6}`):**
`{0: 869, 1: 2878, 2: 218, 3: 29, 4: 6}`, max 4 transport steps,
**4000/4000 land in the open interval $(3/2,2)$, 0 on a seed, 0 failures.**
So 3131 of 4000 samples now genuinely exercise the transport (was ~1310), and
**zero** samples land in the previously-unsupported region $(2,3]$.

### F5 — §5.4's conclusion inverted in the paper's own metric. **REPAIRED** (referee's drafted general formula).
*Locations:* §5.4 (section retitled and rewritten); §1.3 forward reference;
Table 8.1; engine 1 check C26 (new).

§5.4 is now "The two ends of the law move in opposite directions", carrying the
two-parameter statement
$N\varepsilon^{1/4}>(\liminf_q q\lVert q\alpha\rVert)^{1/2}$ and
$N\varepsilon^{1/4}\to(\rho/(\alpha-\alpha'))^{1/2}$, with a four-cell table:
$\sqrt5\mapsto(0.4729,\,0.9732)$, $\varphi\mapsto(0.6687,\,0.8507)$. The false
sentences "twice as hard" and "$\sqrt5$ is a factor 2 cheaper" are gone; the
liminf ratio 2 survives, correctly scoped to liminfs.

New check C26 recomputes all four constants: the two floors in closed form
($20^{-1/4}$, $5^{-1/4}$, ratio exactly $\sqrt2$) and the two attained constants
**from the actual two-block construction** (deficit as the product of the two
one-sided errors) along 40 convergents of $\sqrt5$ and 90 of $\varphi$ in
140-digit `Decimal` — not by evaluating the formula. Tails agree with
$0.9732489894677302$ and $0.8506508083520399$ to $<10^{-25}$; the attained ratio
is $0.874032$, i.e. $\varphi$ is $12.6\%$ cheaper. C25's label was rescoped to
liminfs and now points at C26.

### F6 — §6.3's closing sentence refuted by §6.4's table. **REPAIRED** (referee's drafted replacement).
*Location:* §6.3, final paragraph.

Replaced with the correct statement: $\Phi_5\in SL_2(\mathbb Z)$ preserves
$\mathbb Q$, so attainment **is** an orbit invariant — an *arithmetic* one — and
what §6.2–§6.3 prove is that **no topological or dynamical** invariant (closure,
termination, periodicity, multiplier, $SL_2$-conjugacy class) decides it. Also
corrected the "takes both values there" clause: $\mathfrak q<0$ at every in-window
parameter (§2.3, C4), and the two witnesses $5/2$ ($\mathfrak q=-1$, inside) and
$4/3$ ($\mathfrak q=+5$, outside) take both values on $\Sigma_5$, never inside
$W$. The Abstract's already-correct sentence was left untouched.

---

## SHOULD-FIX

### F7 — Shulman. **REPAIRED.**
References: `[Shu07] T. Shulman, …, Proc. Amer. Math. Soc. 137 (2009), 115–122;
arXiv:0707.3053.` "his Theorem 15" → "her Theorem 15" (Lemma 4.7); engine 3's T3
label likewise ("her Thm 15", with the PAMS coordinates). §7.3 now also records
that Shulman *uses* [KRS03] for exactly our statement, with matching volume/year/
pages — the "primary-by-proxy" strengthening the referee suggested. The SECONDARY
label is retained.

### F8 — DPP Thm. 4.2 / Cor. 4.4 attribution. **REPAIRED.** §1.1, verbatim as
drafted: Thm. 4.2 gives $C_q^s(5,2)$ (synchronous), Cor. 4.4 gives $C_q(5,2)$,
$C_{qs}(5,2)$ and $C_{qs}\ne C_{qa}$.

### F9 — "the constant is pinned". **REPAIRED.** Abstract now says "bracketed to a
factor $2.176$", names the convention, and states explicitly that $D$ is a minimum
over all carriers so $0.9732489895$ is the sharpest *attained* constant, not a
matching lower bound. §5.2: "the sharpest *attained* one", with a sentence naming
what is not ruled out (non-convergent straddling pairs, $\ge3$-block carriers) and
pointing at Remark 3.5.

### F10 — "everything else is an identity". **REPAIRED.** Remark 3.5 rewritten
along the referee's draft: one controlled lossy step (factor
$(5/\sqrt{20})^{1/2}=1.0574$) **plus two strict inequalities** (dropped
within-block variance, and $q_l\le Q$ strict at the §4.2 optimum where
$k_n<k_{n+1}=Q$), residual factor $0.9732/0.4729=2.058$ even with the tight
constant. The remark's conclusion (the gap is genuine) is retained.

### F11 — universal quantifiers on finite computation. **REPAIRED**, option (a) —
both lemmas now have proofs.
*Locations:* Lemma 4.5's proof; Lemma 4.6's proof; §4.3 verification notes;
Table 8.1.

**[DEVIATION 3 — the referee's drafted induction does not close.]** The verdict
proposes: "$b_{j+1}=\alpha-(3-b_j-k_j\epsilon)$ keeps $b_j\in[1,\alpha]$ and
decreases $3l-m-\sum_{i\le j}k_i$ by $k_j\ge1$, so the recursion terminates in
$\le 3l-m-1$ steps". The first half is right and is used. The second half is a
budget bound, not the conclusion: the recursion runs a *prescribed* $s=m-l$ steps,
and what must be proved is that the terminal residue is exactly $\epsilon$ —
equivalently $\sum_j k_j=3l-m-1$. Monotone decrease alone does not give this. The
implemented proof is therefore stronger:

1. *Legality.* $u_j:=3-b_j\in[2-\epsilon,2]$ by induction, so
   $u_j/\epsilon\in(1,4)$ (using $\tfrac12<\epsilon<1$, i.e. $\alpha\in(3/2,2)$),
   hence $k_j=\lceil u_j/\epsilon\rceil-1\in\{1,2,3\}$ exists and is unique, and
   $b_{j+1}\in[1,\alpha)$ — exactly [KRS02, Prop. 5]'s hypothesis.
2. *Termination.* Working in $\mathbb R/\epsilon\mathbb Z$:
   $u_{j+1}=(2-\epsilon)+r_j\equiv 2+r_j$, so $r_j\equiv 2j\pmod\epsilon$. At
   $j=s$, $2s=2l\cdot\epsilon\in\epsilon\mathbb Z$, so $r_s\equiv0$; with
   $r_s\in(0,\epsilon]$ this forces $r_s=\epsilon$ exactly. (This is where
   $\epsilon=s/l$ — i.e. the base interval — enters.)
3. *Dimension.* Telescoping $b_{j+1}=b_j+(k_j+1)\epsilon-2$ with $r_s=\epsilon$
   gives $\sum k_j=2l-s-1=3l-m-1$, hence $\dim=\sum k_j+s+1=2l$.

Lemma 4.6 likewise now has a proof, not a sample: (a) each of $\Phi^\pm,T$ carries
"$d=2\times$denominator" to itself, with the lowest-terms argument
$\gcd(4p-5q,p-q)\mid\gcd(q,p)=1$ written out; (b) every in-window rational reaches
$[3/2,2]$ — one $T$ if $\alpha>3$, one $\Phi^+$ if $\alpha\in(2,3]$, then $\Phi^-$
which strictly halves the denominator, so at most $\log_2 q$ steps; (c) the two
boundary seeds are exhibited. K1–K3 and T1 are re-presented as independent
confirmation rather than support; T2 is presented as what it is — an exhaustive
proof of the transport step for all in-window $p/q$ with $q<400$.

### F12 — §7.1 qualifier whipsaw + undisclosed self-citation. **REPAIRED.**
Hedges ("appears to have", "would give") deleted; the result is stated once in the
tense the companion supports. Added a **Disclosure** paragraph: [I3322] is our own
release, its certificate chain is independent of this paper's engines, no number
in §7.1 is re-derived here and Table 8.1 has no row for it. The referee's
observation about the first rate being $14\%$ off the limit is now *in the text*
(all four successive rates printed) rather than hidden by "converging to".
References: `[I3322]` given an author line (`[the present authors]`, pending the
paper's author block — logged as editorial to-do 6) and the version-of-record DOI
`10.5281/zenodo.21799071`, now agreeing with §7.1.

### F13 — §8's three claims about the verification stack. **REPAIRED** (all three).
*Location:* §8 opening; Table 8.1; engine 2 (K4–K5, new); engine 3 (float removed).

1. *"Every numbered claim is a citation or a machine check"* → replaced with
   "every numbered **arithmetic** claim in §§2–4 and §6", followed by an explicit
   **list of what is not machine-checked** (§5.2's actual-dimension uniform
   constant, §5.3's Open Lemma, §5.4's Liouville remark, all of §7.1, Lemma 4.7,
   Cor. 4.8's interval). Table 8.1 gained six *not checked* rows so the gaps are
   visible in the table, not only in the prose.
2. *"Share no number field"* → replaced with the true statement: all three use
   $\mathbb Q$; engines 2–3 do not use the quadratic or cyclotomic arithmetic of
   engine 1. Engine 3's `BETA = (5 - 5**0.5)/2` float has been **deleted**: window
   membership is now the exact integer test $p^2-5pq+5q^2\le0$ (the Tits form), so
   engine 3 contains no floating point at all. Engine 1's remaining load-bearing
   float comparisons (C9, C15) were moved to 80-digit `Decimal`.
3. *"Independent"* → replaced with "engine 3 consumes engine 2's conclusion and is
   **sequential**, not independent" (also stated in engine 3's docstring), and the
   resulting gap — no claim checked twice — was **closed**, not merely disclosed:
   new checks **K4–K5** in engine 2 re-derive all nine rows of the §4.2 table and
   both of Theorem B's tolerances by rational interval arithmetic. $\sqrt5$ is
   bracketed by two rationals verified by the integer comparison $lo^2<5<hi^2$
   (width $<10^{-149}$); $\varepsilon$ is bracketed with an asserted
   concavity/monotonicity side condition; every conclusion is an integer
   comparison of fourth powers. No $\mathbb Q(\sqrt5)$, no `Decimal`, no float.
   K5 also independently reproduces the F2 discrimination ($N=305$ fails $5e{-7}$,
   $N\ge1292$ passes).

   *Implementation note:* placed inside engine 2 rather than as a fourth file,
   since engine 2 was already the $\mathbb Q$-only engine; the algorithm and the
   number representation are disjoint from engine 1's, which is what the finding
   asks for.

### F14 — the drafting note's "nothing is strengthened" + two dead cross-references. **REPAIRED.**
*Location:* the `DRAFTING NOTE` block; Remark 3.6; Table 8.1; engine 1 check C5b
(new).

The note now carries an **Audit of the rendering** listing the three deliberate
departures: (1) *strengthened* — Theorem A at the reduced denominator (F3);
(2) *route changed* — the source's "$\mathbb Z_5$-shift, verified at $q=4,17,72$"
is not used anywhere; the paper proves $q\le d_5\le 2q$ outright and attributes
$=q$ to [KRS03] via [Shu07]; (3) *weakened* — the six-figure claim (F2), with the
false version named as false.

"Remark 3.6 … is check C5" was **false** and is repaired the way the referee's
first option asks: new fixture **C5b**, a two-block carrier
(block A = the $M_3$ four-vector tight frame padded with a zero, marginals
$\tfrac13,\tfrac13,\tfrac13,\tfrac13,0$; block B = the $M_2$ pentagon, marginals
all $\tfrac12$) with weight $\mu$ fixed by $\mu\cdot\tfrac43+(1-\mu)\cdot\tfrac52
=\sqrt5$. Its five marginals are **unequal** ($0.4623$ vs $0.3869$) and average
exactly to $t_\ast$; the check verifies the mean-marginal condition exactly, the
deficit identity $(\tfrac52-\sqrt5)(\sqrt5-\tfrac43)=0.2382606$, and that
Theorem A's bound $\varepsilon>1/(25Q^4)$ still holds. Remark 3.6 and Table 8.1
now cite C5b, and Remark 3.6 explains in place why C5 cannot support it.

---

## HYGIENE

### F15 — paraphrase inside quotation marks. **REPAIRED.** §3.1 now quotes DPP's
full sentence ("Since this algebra has a unique tracial state, and this trace takes
rational values on all projections, we see that this value of $\lambda$ must be
rational."). The verbatim §1.2 block quote was left untouched, as instructed.

### F16 — Coladangelo–Stark missing. **REPAIRED.** Added `[CS20] A. Coladangelo,
J. Stark, An inherently infinite-dimensional quantum correlation, Nat. Commun. 11,
3335 (2020)` to the References, cited as `[CS20]` in §7.2, and acknowledged
arXiv:1904.02350 (non-closure via embezzlement, likewise with no rate) in the same
list.

### F17 — [Kru02] translation. **REPAIRED.** Added "English transl., Ukrainian
Math. J. **54** (2002), no. 6, 967–978", adopted the translation's own title
("Coxeter functors for one class of $\ast$-quivers"), and noted in the entry that
[KRS02]'s and [Shu07]'s renderings differ.

### F18 — infimum identified before it is proved. **REPAIRED.** §2.4 gained the
referee's sentence: $f_{\mathrm{vect}}(t_\ast)$ being the infimum (not merely a
lower bound) is a corollary of Theorem B; until §4 the reader may read
$\varepsilon$ as the excess over the vectorial bound.

### F19 — total Hilbert dimension convention absent. **REPAIRED.** §5.1 is now
"The three dimension conventions" with a third row $\sum_l n_l$
(lower $0.4472$; upper $9.732$–$19.46$; uniform $41.2$–$82.4$; bracket
$21.8$–$43.5$) and the two-line justification ($\max\le\sum$ for the lower bound;
two blocks so $\sum\le2\max$ for the upper). §2.4 and §1.3 updated from "two
conventions" to "three".

### F20 — unproved structural claim in §2.2. **REPAIRED**, referee's wording:
"…hyperbolic for $n\ge5$ — matching, and we suggest explaining, the trichotomy of
$\Sigma_n$. We state that match as an *organising observation*, not a derivation",
with an added sentence that no implication is proved and none is used below.

### F21 — "Theorem B (upper bound, attained)". **REPAIRED** at all three sites:
the theorem header, Theorem 1.1(B), and §7.1's comparison table, all now "the
exponent and the constant are achieved along an explicit family".

### F22 — three objects called $q$. **REPAIRED.** The multiplier of $\Phi_5$ is
renamed $\kappa$ in §2.2, with a parenthetical saying why ($q$ = denominator from
Lemma 3.3 on, $\mathfrak q$ = Tits form). The engine-1 variable `q_mult` was
renamed `kappa` and its printed label with it.

### F23 — five statement slips. **ALL REPAIRED.**
- Theorem A: "Consequently $D(\varepsilon)\ \ge$" → "$>$".
- Abstract "the least dimension" → "the least *block* dimension", with a pointer
  to §1.3/§5.1 (reconciled with F19).
- Prop. 6.1: "$M_3^{\oplus5}=M_{15}$" → "$\bigoplus_5 M_3\subset M_{15}$".
- Theorem 1.1's box now names the convention of its two constants.
- §5.1's actual-dimension uniform cell now carries the number
  ($20.6$–$41.2$), as every other cell does.

### F24 — three checks certifying less than their labels. **ALL REPAIRED.**
- **C1** was an algebraic tautology. Replaced with a real test of the label:
  DPP Prop. 4.1's three branches $\{0,\ nt(nt-1),\ (n^2-n)(2t-1)\}$ are formed and
  the middle branch is verified to be their **maximum exactly on
  $[1/n,(n-1)/n]$** (and not outside it), $n=3..8$ on a 121-point exact grid.
  §1.1 and Table 8.1's row were rewritten to match what is now checked.
- **C8** dead code (`worst`, and the meaningless
  `F(qd*abs(five_q2 - m*m), 5*qd)`) deleted. The exhaustive $q\le200\,000$ sweep
  is untouched.
- **C20** vacuous conjunct `(5*q) % 1 == 0` deleted; the check now verifies the
  label's *conclusion*, the equivalence
  $5q\mid pd \iff \big(q\mid d$ and $(5\mid p$ or $5\mid d/q)\big)$, over seven
  $p/q$ and $d=1..399$, with an assertion that both truth values occur. Lemma 4.3's
  statement was sharpened to "$5\mid(d/q)$, in particular $5\mid d$".
- **C10** now sweeps 22 convergent denominators, asserts monotone approach to
  $1/\sqrt{20}$, and — the substantive part — adds a **second** assertion that
  $\inf_q q\lVert q\sqrt5\rVert<1/\sqrt{20}$ (at $q=4$: $0.2229124$), so the word
  "asymptotically" in §3.3 is certified as load-bearing. §3.3 and Table 8.1 say so
  in the text.

### F25 — Cor. 4.8's "$5\nmid p$" asserted but never proved. **REPAIRED.** Added
the proof as a parenthetical after Lemma 4.7: modulo 5 the pair
$(h_n,h_{n+1})$ evolves by $(a,b)\mapsto(b,a-b)$ from $(2,4)$, giving the
4-cycle $(2,4)\to(4,3)\to(3,1)\to(1,2)$, so $h_n\equiv2,4,3,1$ and never $0$.
Asserted in C14 (62 terms, plus the periodicity).

### F26 — unreproducible citing-set sweep. **REPAIRED by disclosure.** A search of
the working repository's records (`[private-workspace]/PRECONDITIONS-REPORT.md` and the
surrounding tree) found **no** record of the API, the query or the date, so naming
them as the referee's repair asks would have meant inventing them. §7.2 item 2 now
reports the sweep as *supporting evidence, not a reproducible check*, states in
place that the API/query/date were not snapshotted and that a citing set is a
moving target, and contrasts it with item 1, which *is* reproducible (the fixed
$57\,125$-byte DPP source). Editorial to-do 3 was rewritten to record that the
metadata is not recoverable and what a re-run must capture (the DPP source hash
was likewise never taken; only the byte count is known).

---

## "ALSO, BEFORE CIRCULATION"

- **Strip the DRAFT banner / DRAFTING NOTE / Editorial to-do.** *Deliberately not
  done, with a marker added instead.* These conflict with F14, whose repair is to
  *correct* the drafting note; and the paper is in a repair round, not being
  circulated. A `STRIP BEFORE CIRCULATION` block was added at the top naming
  exactly the three items to delete and why they are retained (so the
  source-statement audit trail survives further rounds). Recorded here so the step
  is not lost.
- **Timings.** §8's "~25 s total" → "~18 s total on the repair-round machine",
  with the note that timings are machine-dependent and are reported, not asserted.
  Engine 2's docstring "~5 s" → "~20 s"; engine 3's "~10 s" → "~2 s"; engine 1's
  "~10 s" → a description of what dominates rather than a number (it runs in
  0.3 s here against the referee's 9 s — the C8 sweep was verified still intact at
  $q\le200\,000$).
- **Engine-1 docstring title.** Aligned to the paper's actual title.

---

## Numbers

**Unchanged** (re-verified this round): all nine rows of the §4.2 table; both
constants $0.9732489895$ and $0.4472135955$; $(2+\sqrt5)^4=321.9968944$; the
uniform constant $4.1226$; the factor $5779$; $(9\sqrt5-20)/2$ and
$(305\sqrt5-682)/68$; §8.2's $1.1236/0.0000/20.1620$; the $\varphi/\sqrt5$ liminf
ratio $2$; the maximum transport depth, 4 steps.

**Changed:**

| quantity | was | now | why |
|---|---|---|---|
| six-figure plateau start | $N=17$ | $N=1292$ | F2 (false claim) |
| plateau decade spans | $3.76$ / $15.05$ (were the table's) | $1.88$ / $7.52$ | F2 |
| C14 tolerance | one, $5\times10^{-3}$ | two, $5\times10^{-3}$ and $5\times10^{-7}$ | F2 |
| rel. deviation at $N=305$ | (verdict) $3.1\times10^{-6}$ | $2.81\times10^{-6}$ | recomputed, two engines |
| rel. deviation at $N=1292$ | (verdict) $1.1\times10^{-8}$ | $1.57\times10^{-7}$ | recomputed, two engines |
| T1 step histogram | $\{0{:}2690,1{:}1057,2{:}218,3{:}29,4{:}6\}$ | $\{0{:}869,1{:}2878,2{:}218,3{:}29,4{:}6\}$ | F4 (loop now reduces to $[3/2,2]$) |
| T1 samples in the unproved region $(2,3]$ | 1821 | **0** | F4 |
| §5.1 denominator lower constant | $\ge0.2236$ | $0.4472$ | F3 (strict improvement) |
| §5.1 actual-dim uniform cell | "$\times(2+\sqrt5)$" | $20.6$–$41.2$ | F23 |
| engine-1 assertion count | 36 | 43 | C5b, C9b, C10b, C14b/c, C15b, C26 |
| engine-2 assertion count | 3 | 6 | K4 (×2), K5 |
| engine-3 assertion count | 3 | 4 | T1 non-circularity |

**New numbers introduced** (all machine-checked): $1.0574=(5/\sqrt{20})^{1/2}$ and
$2.058=0.9732/0.4729$ (Remark 3.5); $10.9$–$21.8$ (actual-dimension bracket);
$9.732$–$19.46$, $41.2$–$82.4$, $21.8$–$43.5$ (total-dimension row); $0.4728708$,
$0.6687403$, $0.8506508$ and the ratio $0.874032$ (§5.4); $0.2229124$ (C10);
$0.2382606$ and marginals $0.4622954/0.3868863$ (C5b).

---

## Dissents

**None.** Every finding F1–F26 was implemented. Three implementations deviate from
the referee's drafted wording or argument, each recorded in place above and each
in the direction of *more* accuracy, not less:

1. **F2** — "monotonically convergent" not adopted (the ratio oscillates).
2. **F2** — two of the verdict's relative deviations corrected against two
   independent engines; the finding's conclusion is unaffected.
3. **F11** — the referee's sketched induction is a budget bound and does not yield
   $\sum_j k_j=3l-m-1$; replaced with a complete proof (legality invariant +
   a mod-$\epsilon$ argument + telescoping).

One conflict inside the verdict was resolved rather than dissented: F14 ("re-word
the drafting note") versus "Also, before circulation: strip the drafting note".
The note was corrected and a `STRIP BEFORE CIRCULATION` marker added; see above.
