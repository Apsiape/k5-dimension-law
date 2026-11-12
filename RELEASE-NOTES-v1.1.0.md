# Release notes — v1.1.0 (2026-11-11)

**PROVED — improvement.** The denominator minimum is exactly
$e_Q=(a_Q-\sqrt5)(\sqrt5-b_Q)$, with Farey neighbours of order $Q$. A
supporting-line identity proves it for every admissible carrier; scalar
neighbour blocks attain it. The sharp denominator liminf and limsup of
$D_{\rm den}(\varepsilon)\varepsilon^{1/4}$ are $0.7434960689$ and
$1.5747499445$. The liminf uses $j=1$ intermediate semiconvergents, including
$Q=21,89,377,\ldots$. The exact fixed-target drift criterion is
$e_Q\le\varepsilon+5(a_Q+b_Q-1)\delta$; its pure-drift liminf and limsup are
$0.3642394613$ and $0.7714715591$. The exact drift threshold in the
denominator convention is proved; Theorem 5.3(a)'s lower bound in every
convention is unchanged.

**PROVED — sharper parameter comparison.** At $\varphi$ the corresponding
exact-marginal constants are $0.8506508084$ and $1.3763819205$: the best-case
constant is higher, the worst-case one lower than at $\sqrt5$.

**FALSE — corrected old assertions.** The old unqualified descriptions of
convergents as extremisers (v1.0.2 §§4.1 and 5.3) are replaced by Farey
neighbours, including intermediate semiconvergents; at $Q=21$ the optimum is
$(47/21,38/17)$. Consecutive convergent deficit ratios (v1.0.2 §5.2) have the
stated limit, not an exact fixed value at finite indices. The old
convergent-only $\varphi$ comparison was literally true and is retained as
historical context, not recorded as a false sentence.

**PROVED — convention clarification.** Denominator minima are denoted
$D_{\rm den}$; unqualified $D$ retains actual block dimension. Cyclic copies
may remain separate blocks, so $D_{\rm den}\le D\le2D_{\rm den}$ on primary
evidence. Conditional on the existing secondary dimension lemma they are
equal. No exact unconditional actual or total dimension constants are claimed.

**COMPUTED — independent verification.** Two newly supplied engines use exact
quadratic-field arithmetic and certified rational intervals. Each checks
42,519 straddling pairs per objective for orders 1–12, reproduces positive
controls $e_4,e_{17},\delta_{17}$, and rejects a planted non-neighbour pair.
The engines agree on all 34 and 26 neighbour-change nodes through order
300,000 for $\sqrt5$ and $\varphi$, respectively. Independently generated
large nodes certify 100 four-node records. Both engines are standard-library
only, run on any platform with `python -B`, and exited 0 in the release run
(`python -I -B`); their JSON outputs and printed transcripts ship in
`verification/`. The three legacy engines are unchanged.

**PROVED — surviving results.** The fourth-root exponent in every dimension
convention, Theorem A's lower bound, the convergent tables and the v1.0.2
drift correction remain valid. This is a release improvement with the limited
textual corrections identified above. Historical release-note addenda make
clear which older constants were superseded.

**Release tree.** `README.md`, `CITATION.cff` and `.zenodo.json` are updated
to v1.1.0. `RELEASE-NOTES-v1.0.0.md` and `RELEASE-NOTES-v1.0.2.md` keep their
original text and gain dated v1.1.0 addenda.
