# Release notes — v1.0.0

First public release. 2026-08-10.

## What ships

A proof, in both directions and with explicit constants, of a dimension law for
the Dykema–Paulsen–Prakash $K_5$ non-closure witness:

```text
D(eps) = Theta(eps^(-1/4))
```

where $D(\varepsilon)$ is the least block dimension of a finite-dimensional
carrier whose value exceeds the infimum by at most $\varepsilon$, at exact
marginals and at $t_\ast = 1/\sqrt5$.

| item | content |
|---|---|
| `paper/PAPER-K5.md` | the paper: eight sections, Theorems A and B, §5 conventions, §6 orbit-vs-attainment negative result, §7 priority and contrast, §8 verification appendix with the claim-to-check table |
| `verification/` | three exact-arithmetic engines, standard library only, 43 + 6 + 4 assertions, exit 0 |
| `review/` | the complete refereeing record — two refutation-first blind rounds, one repair round — plus a protocol preface |
| `CITATION.cff`, `.zenodo.json` | citation and archive metadata |
| `LICENSE.md`, `LICENSES/` | CC BY 4.0 for prose and paper, MIT for the engines |

## The two ends of the law

- **Theorem A (lower, unconditional).** Every carrier at exact marginals has
  deficit $\varepsilon > 1/(25Q^4)$, with $Q$ the largest reduced denominator of
  a block value; equivalently $Q\varepsilon^{1/4} > 25^{-1/4} = 0.4472135955$.
  Proved through the law of total variance, so no block-scalar hypothesis, no
  equal-rank hypothesis and no bound on the number of blocks is used. Because
  $q_l \mid n_l$, the same constant is a floor in every dimension convention,
  and the lower bound does not pass through Lemma 4.6 at all.
- **Theorem B (upper, attained).** Two-block carriers built from consecutive
  continued-fraction convergents of $\sqrt5$ give
  $N\varepsilon^{1/4} \to ((2+\sqrt5)/(2\sqrt5))^{1/2} = 0.9732489895$,
  computed across $N = 17 \to 98\,209$ and
  $\varepsilon = 1.08\times10^{-5} \to 9.64\times10^{-21}$, flat to six
  significant figures from $N = 1292$ on. The mechanism is the exact identity
  $\varepsilon = (\lambda_1-\sqrt5)(\sqrt5-\lambda_2)$: the deficit is the
  product of the two one-sided approximation errors.

Together: the law is bracketed to a factor **2.176** in the denominator
convention. That is a bracket, not a pin — $D$ is a minimum over all carriers
and $0.9732489895$ is the sharpest *attained* constant, not a matching lower
bound.

## What is explicitly not claimed in v1.0.0

- The **drift regime**. All results assume exact marginals. §5.3's conjecture
  $D(\varepsilon,\delta) = \Theta(\min(\varepsilon^{-1/4},\delta^{-1/2}))$ is
  stated as an Open Lemma and is not proved.
- The **general quadratic-irrational formula** of §5.4 is stated as the shape of
  the answer; its ingredients are proved here only for $\sqrt5$.
- **Cor. 4.8's actual-dimension constant** is an interval
  $4.866 \le C_{\mathrm{act}} \le 9.732$, not a value, because Lemma 4.7 is a
  SECONDARY citation ([KRS03] via [Shu07], source not obtained in full). The
  paper's own Lemma 4.6 gives $q \le d_5(p/q) \le 2q$ from primary text plus two
  exact machine checks; the residue $q$ versus $2q$ is the one loose constant in
  the paper and is labelled as such.
- **Priority** is labelled *new, provisional* — no evidence found, not proved
  absent. §7.2 states the sweep as it ran, including one component disclosed as
  supporting evidence rather than a reproducible check.
- **Items not machine-checked** are named in place in Table 8.1 rather than
  passed over.

## Verification

Three engines, standard library only, no dependencies to install:

```sh
cd verification && python verify_dimension_law.py && python verify_krs_dimension.py && python verify_transport_dimension.py
```

Expect 43, 6 and 4 assertions and exit 0 from each. Roughly 20 seconds in
total, dominated by engine 2's exhaustive 7 921-case recursion.

Engine 3 is *sequential* on engine 2, not independent of it — engine 3 consumes
engine 2's base-interval dimension $2l$ as an input. That is disclosed rather
than glossed. The gap it would otherwise leave (no claim checked twice) is
closed by checks K4–K5 in engine 2, which re-derive the §4.2 table by rational
interval arithmetic without ever forming an element of $\mathbb{Q}(\sqrt5)$ and
without calling `Decimal`. The §4.2 table and Theorem B's six-figure plateau are
therefore certified by two engines sharing no number representation and no
verification code; the one shared ingredient is the convergent recursion that
generates the $\lambda$ pairs.

## Review history

Two refutation-first blind rounds either side of a repair round; mutation
testing of the checks; freeze checks on the reviewed state. 26 findings raised,
26 repaired, 0 dissents; 24 of 26 confirmed faithful on audit, one honest
substitution, one softening reopened and closed, zero missing, zero
overcorrected; four residual conditions raised in the confirm round, all four
discharged. Final ruling: **PROMOTE**.

No arithmetic in the paper was found to be wrong in any round. What the rounds
killed was the paper misdescribing its own arithmetic and its own engines — a
false flatness claim, a cross-convention constant comparison, a constant wrong
in its fifth significant figure, an engine test that did not test its lemma, and
check labels promising more than they asserted. All corrected in the shipped
text; all still legible in `review/`.

Three blocks of drafting apparatus that the working draft itself designated
`STRIP BEFORE CIRCULATION` — a draft banner, an internal rendering-audit note,
and an editorial to-do list — were removed for this public edition. Nothing
mathematical was touched; the removal is recorded in a note at the head of the
paper.

## DOI

None yet. `CITATION.cff` and `.zenodo.json` carry no `doi` field; both should be
updated when one is minted.
