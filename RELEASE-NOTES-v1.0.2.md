# Release notes — v1.0.2 (2026-09-24)

Correction release for Section 5.3. Theorems A and B, the verification
engines' existing checks C1–C26, and every constant of the exact-marginal
law are unchanged. Five checks (C27–C29) are added.

## The correction (paper/PAPER-K5.md, Section 5.3)

Versions 1.0.0–1.0.1 stated an Open Lemma, explicitly "not proved and not
claimed": if the marginals are allowed to drift by delta, the cost was
conjectured to be Omega(delta^(-1/2)), giving
D(eps, delta) = Theta(min(eps^(-1/4), delta^(-1/2))).

**That conjecture was false** under the paper's own definition of the
deficit (value minus the infimum at the target t* = 1/sqrt5). The correct
law is

    D(eps, delta) = Theta(min(eps^(-1/4), delta^(-1/4)))

(Theorem 5.3), the same fourth root as the exact-marginal law.

**Why.** Against the fixed target, the deficit of a carrier with mean
marginal m/5 is Var_tau(S) + (m - sqrt5)(m + sqrt5 - 1). A mean slightly
below sqrt5 makes the second term negative and pays for the variance of a
straddling two-block pair; for such a pair the deficit is affine in m and
can be made exactly zero (Proposition 5.2). The refuting carrier uses the
convergents 9/4 and 38/17 at denominator 17: its value is exactly
5 - sqrt5, and every marginal is off by (305 sqrt5 - 682)/1185 = 6.19e-7.
Along consecutive convergent pairs N delta^(1/4) -> 0.4767956449 and
N delta^(1/2) -> 0, so no delta^(-1/2) bound can hold. The lower bound is
Theorem A's argument with a drift term added, constant 0.1458 in every
dimension convention.

**What survives.** The conjectured formula is the answer to a different
question: if the deficit is referenced to the carrier's own mean marginal
(the variance alone), then D_V = Theta(min(eps^(-1/4), delta^(-1/2)))
holds and is a three-line corollary of Theorem A (Proposition 5.4). The
paper's definition and the physical "marginals and all" question are both
fixed-target questions.

**Remark 5.5** records that after the ten-map symmetrisation over the
affine group of Z_5, the zero-deficit carriers reproduce every pair
probability of the target exactly and miss only the marginals.

## Verification

`verification/verify_dimension_law.py` gains checks C27 (Proposition 5.2
and the explicit carrier, exact in Q(sqrt5)), C28 (the drift family along
40 convergent pairs in 80-digit Decimal) and C29 (the constants of Theorem
5.3(a) and Proposition 5.4, the deficit identity on non-scalar fixtures,
and the convergent bound). Expect 48, 6 and 4 assertions, all exit 0.

## Provenance

The error was found on 2026-09-24 while transporting the paper's method to
the Musat–Rørdam Schur channel, whose exact finite realisations are five
projections summing to (5 sqrt2/3) times the identity. Two independent
derivations reached the same counterexample and the same corrected law;
the arithmetic was then recomputed in exact form for this release. As in
v1.0.1, the correction is filed openly and the superseded statement is
kept visible in Section 5.3.
