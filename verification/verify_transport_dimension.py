#!/usr/bin/env python3
r"""
VERIFICATION APPENDIX, ENGINE 3 --- the realisation-dimension lemma, part 2:
the Coxeter dimension maps carry `d = 2q` across the whole n = 5 window.

Checks T1-T3 of the paper's Table 8.1.

NOT INDEPENDENT OF ENGINE 2 (disclosed in paper section 8): the base-interval
dimension `2l` consumed below is engine 2's conclusion, so this engine is
SEQUENTIAL on `verify_krs_dimension.py`, not independent of it.  What it does
not share with engine 1 is the arithmetic: only `fractions.Fraction` over Q and
exact integers are used here -- there is no Q(sqrt5), no Q(zeta_5), no Decimal,
and (since repair round R1) no floating point at all.  Window membership is the
exact integer condition p^2 - 5 p q + 5 q^2 <= 0, which is the Tits form.

SOURCE (primary, English, open access: Yu. Samoilenko, "When is a sum of
projections equal to a scalar operator?", J. Nonlinear Math. Phys. 11
Suppl. (2004) 92-103, p. 99, reproducing KRS 2002 Theorem 2 and eq. (2.5)):

  the generalized dimension of a representation of P_{n,alpha} on H is
  (d; d_1,...,d_n) with d = dim H, d_i = dim H_i, and
      S(d; d_1..d_n) = (sum_i d_i - d; d_1..d_n),
      T(d; d_1..d_n) = (d; d - d_1, ..., d - d_n).                   (2.5)

Since sum_i d_i = alpha d for a representation of P_{n,alpha}, (2.5) gives,
for n = 5,

    Phi^+ = S o T :  alpha -> 1 + 1/(4 - alpha),   d -> (4 - alpha) d
    Phi^- = T o S :  alpha -> 4 - 1/(alpha - 1),   d -> (alpha - 1) d
    T           :  alpha -> 5 - alpha,             d -> d

On the base interval (3/2, 2), KRS's own Theorem 6 construction realises
alpha = m/l in dimension 2l (engine 2, `verify_krs_dimension.py`).  The
claim checked here: transporting an arbitrary in-window rational p/q into
the base interval and pulling the construction back by these maps lands on
dimension exactly 2q -- i.e. the bound d_5(p/q) <= 2q holds on the WHOLE
continuous spectrum, not just on (3/2, 2).

REPAIR ROUND R1, finding F4.  The previous version of T1 reduced into
[3/2, 3] and not into [3/2, 2].  That was wrong in two ways at once: 2690 of
4000 samples took ZERO transport steps (so `d = 2q` was assigned by this
script rather than derived), and 1821 of 4000 landed in (2, 3], where
Lemma 4.5 -- proved only on (3/2, 2) -- says nothing.  The pair {T, Phi^-}
used there cannot leave (2,3): T maps (2,3) to itself and Phi^- moves upward
on it.  The fix is Phi^+, which reduces (2,3] into (3/2,2] in ONE step.  The
loop below therefore reduces into [3/2, 2] using

    a > 3        : T       (a -> 5 - a,          lands in (lam_-, 2))
    2 < a <= 3   : Phi^+   (a -> 1 + 1/(4-a),    lands in (3/2, 2])
    a < 3/2      : Phi^-   (a -> 4 - 1/(a-1),    denominator drops below q/2)

and asserts (i) the landing point is in [3/2, 2], (ii) at least one transport
step was taken for every sample outside [3/2, 2], (iii) the pulled-back
dimension is exactly 2q.  The step histogram is reported.

The arithmetic reason (checked as T2): for alpha = p/q in lowest terms,
    Phi^-(p/q) = (4p - 5q)/(p - q)  and  gcd(4p-5q, p-q) | gcd(q, p-q) = 1,
so the image is already in lowest terms with denominator p - q, and the
dimension map sends 2q -> ((p-q)/q) * 2q = 2(p-q) = 2 * (new denominator).
Identically for Phi^+ (p/q -> (5q-p)/(4q-p), d -> 2(4q-p)) and for T
(p/q -> (5q-p)/q, d fixed).

stdlib only.  Exit 0 on full pass.  Runtime: ~2 s.
"""

from __future__ import annotations

import random
import sys
from fractions import Fraction as F
from math import gcd

FAILURES: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> bool:
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"   {detail}" if detail else ""))
    if not cond:
        FAILURES.append(label)
    return cond


def in_window(a: F) -> bool:
    """alpha = p/q lies in W = [(5-sqrt5)/2, (5+sqrt5)/2] iff the Tits form is
    <= 0, i.e. iff p^2 - 5 p q + 5 q^2 <= 0.  EXACT INTEGER TEST -- no float,
    no sqrt5.  (alpha^2 - 5 alpha + 5 <= 0, cleared of denominators.)"""
    p, q = a.numerator, a.denominator
    return p * p - 5 * p * q + 5 * q * q <= 0


def phi_plus(a: F) -> F:
    return 1 + F(1, 1) / (4 - a)


def phi_minus(a: F) -> F:
    return 4 - F(1, 1) / (a - 1)


def T(a: F) -> F:
    return 5 - a


def main() -> int:
    print(__doc__)
    print("=" * 78)
    print("Coxeter transport of the realisation dimension, n = 5")
    print("=" * 78)

    # ----- T2: the lowest-terms / dimension bookkeeping, purely arithmetic.
    ok = True
    for q in range(1, 400):
        for p in range(1, 5 * q):
            if gcd(p, q) != 1:
                continue
            a = F(p, q)
            if not in_window(a):
                continue
            if a > 1:
                im = phi_minus(a)
                if im.denominator != abs(p - q) or 2 * q * (a - 1) != 2 * im.denominator:
                    ok = False
            if a < 4:
                im = phi_plus(a)
                if im.denominator != abs(4 * q - p) or 2 * q * (4 - a) != 2 * im.denominator:
                    ok = False
            imT = T(a)
            if imT.denominator != q:
                ok = False
        if not ok:
            break
    check("T2  Phi^- : p/q -> (4p-5q)/(p-q) is already in lowest terms and the "
          "dimension map 2q -> (alpha-1)*2q = 2(p-q) tracks the new denominator; "
          "identically for Phi^+ and T (all in-window p/q with q < 400)", ok)

    # ----- T1: transport a random sample into the PROVED base interval
    #           [3/2, 2] -- NOT [3/2, 3], see the R1 note in the docstring --
    #           attach the base dimension 2 * denominator, pull back, and
    #           demand d = 2q.
    random.seed(7)
    cands: list[F] = []
    for q in range(2, 400):
        for p in range(1, 5 * q):
            a = F(p, q)
            if a.denominator != q:
                continue
            if in_window(a):
                cands.append(a)
    sample = random.sample(cands, 4000)

    def in_base(a: F) -> bool:
        return F(3, 2) <= a <= 2

    bad: list[tuple] = []
    tested = 0
    maxsteps = 0
    hist_steps: dict[int, int] = {}
    landed_open = 0          # landed in the OPEN interval (3/2, 2): Lemma 4.5
    landed_seed = 0          # landed on a seed 3/2 or 2
    for a0 in sample:
        a = a0
        steps = 0
        hist: list[tuple[str, F]] = []
        while not in_base(a):
            if a < F(3, 2):
                a2, op = phi_minus(a), "M"       # denominator strictly drops
            elif a > 3:
                a2, op = T(a), "T"               # reflect into (lam_-, 2)
            else:                                # 2 < a <= 3
                a2, op = phi_plus(a), "P"        # ONE step into (3/2, 2]
            hist.append((op, a))
            a = a2
            steps += 1
            if steps > 200:
                break
        if not in_base(a):
            bad.append(("no landing in [3/2,2]", a0, a))
            continue
        if a in (F(3, 2), F(2)):
            landed_seed += 1
        else:
            landed_open += 1
        # F4 assertion: the check must not be circular.  A sample that starts
        # outside the base interval MUST have taken at least one transport step.
        if (not in_base(a0)) and steps == 0:
            bad.append(("zero steps from outside the base interval", a0))
            continue
        # base dimension, uniformly 2 * denominator:
        #   alpha in (3/2,2) -> Lemma 4.5 (engine 2), dimension exactly 2l;
        #   alpha = 3/2      -> the three coplanar rank-1 projections at 120
        #                        degrees in M_2, padded with two zeros, doubled;
        #   alpha = 2        -> 1 + 1 + 0 + 0 + 0 in M_1, doubled.
        d = 2 * a.denominator
        # pull the dimension back along the recorded transport
        for op, prev in reversed(hist):
            if op == "M":
                assert phi_minus(prev) == a
                num = prev - 1                   # Phi^- : d -> (alpha-1) d
            elif op == "P":
                assert phi_plus(prev) == a
                num = 4 - prev                   # Phi^+ : d -> (4-alpha) d
            else:
                assert T(prev) == a
                num = F(1)                       # T     : d -> d
            d_prev = F(d) / num
            if d_prev.denominator != 1:
                bad.append(("non-integral pullback", a0, prev, d))
                break
            d = int(d_prev)
            a = prev
        else:
            tested += 1
            maxsteps = max(maxsteps, steps)
            hist_steps[steps] = hist_steps.get(steps, 0) + 1
            if d != 2 * a0.denominator:
                bad.append(("dim != 2q", a0, d))

    zero_step = hist_steps.get(0, 0)
    check(f"T1  transporting 4000 random in-window rationals into the PROVED "
          f"base interval [3/2, 2] (never into (2,3], where Lemma 4.5 says "
          f"nothing) and pulling the KRS construction back lands on dimension "
          f"exactly 2q  ({tested} completed, {len(bad)} failures, "
          f"max {maxsteps} transport steps; step histogram "
          f"{dict(sorted(hist_steps.items()))}; {landed_open} landed in the "
          f"open interval, {landed_seed} on a seed)",
          len(bad) == 0 and tested >= 3990,
          "; ".join(str(b) for b in bad[:4]))
    check(f"T1  and the check is not circular: every sample that starts OUTSIDE "
          f"[3/2, 2] takes at least one transport step "
          f"({zero_step} of {tested} samples were already in the base interval, "
          f"where d = 2q is Lemma 4.5 itself and nothing is being assumed)",
          all(b[0] != "zero steps from outside the base interval" for b in bad)
          and zero_step == sum(1 for a0 in sample if in_base(a0)),
          f"zero-step samples = {zero_step}")

    # ----- T3: the trace bound, and what it leaves open.
    ok = True
    for (p, q) in ((9, 4), (38, 17), (161, 72), (682, 305), (5, 2), (4, 3)):
        for d in range(1, 400):
            if ((F(p, q) * d).denominator == 1) != (d % q == 0):
                ok = False
    check("T3  trace bound q | d_5(p/q); with T1 this pins d_5(p/q) in {q, 2q} "
          "on primary evidence alone.  KRS 2003 (LAA 370, 217-225), quoted by "
          "T. Shulman (arXiv:0707.3053 = Proc. Amer. Math. Soc. 137 (2009) "
          "115-122, proof of her Thm 15) as giving a realisation in "
          "q-dimensional space, closes it to = q; that citation is SECONDARY "
          "here and is flagged as such in the paper.", ok)

    print()
    print("=" * 78)
    if FAILURES:
        for f in FAILURES:
            print("  FAILED: " + f)
        return 1
    print("  all checks passed")
    print()
    print("  CONSEQUENCE (paper Lemma 4.6 + Section 5).  q <= d_5(p/q) <= 2q, so")
    print("  the exponent -1/4 is convention-independent and the constant in the")
    print("  actual-dimension convention is pinned to within a factor 2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
