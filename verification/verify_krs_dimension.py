#!/usr/bin/env python3
r"""
VERIFICATION APPENDIX, ENGINE 2 --- (1) KRS 2002's own construction has
dimension exactly 2l on the base interval; (2) an INDEPENDENT re-derivation
of the paper's Section 4.2 table by rational interval arithmetic.

Checks K1-K5 of the paper's Table 8.1.  Second engine on Lemma 4.6
(d_5(p/q) <= 2q), independent of engine 1 (`verify_dimension_law.py`): it
does not use Q(sqrt5) at all, only Fraction arithmetic over Q, and it
re-executes the INCUMBENT's construction rather than any construction of
ours.

K4-K5 were added in repair round R1 (finding F13).  Before them, NO claim of
the paper was checked by two engines: engine 3 consumes engine 2's conclusion
and is sequential on it, and engine 1 was alone on Sections 3-4.  K4-K5 close
that gap on the paper's most load-bearing table.  They re-derive every row of
Section 4.2 -- and both tolerances of Theorem B's flatness claim -- WITHOUT
forming a single element of Q(sqrt5) and WITHOUT calling Decimal: sqrt5 is
bracketed between two rationals verified by the exact integer comparisons
lo^2 < 5 < hi^2, and every conclusion is a comparison of integers.

SOURCE (primary, read in the Russian original: S. Kruglyak, V. Rabanovich,
Yu. Samoilenko, "O summakh proektorov", Funkts. Anal. Prilozh. 36:3 (2002)
20-35 = Funct. Anal. Appl. 36 (2002) 182-195; the same Section 1 appears
verbatim in English in Yu. Samoilenko, "When is a sum of projections equal
to a scalar operator?", J. Nonlinear Math. Phys. 11 Suppl. (2004) 92-103):

  Definition 1 ("sewing"/"skleika", A ~+ B): an m x m matrix A sewn to an
    l x l matrix B is the (m+l-1) x (m+l-1) matrix overlapping a_{mm} with
    b_{11}.  If P_1..P_k are (sums of) projections then so is the sewing,
    with the SAME number of summands; dimensions add and lose 1 per join.
    Sewing with the 1x1 matrix (1) does not change the dimension.
  Proposition 5: for 1 <= b <= alpha there is k in {1,2,3} with
    0 < 3 - b - k eps <= eps (eps = alpha - 1), and FIVE explicit
    projections summing to diag(b, alpha [k times], 3 - b - k eps)
    -- a (k+2) x (k+2) matrix.
  Lemma 7 recursion: b_1 = alpha, b_{j+1} = alpha - (3 - b_j - k_j eps).
  Theorem 6: R_1 = P_{11} ~+ ... ~+ P_{1s} ~+ (1), R_i = P_{i1} ~+ ... ~+
    P_{is} for i = 2..5, with s = m - l.

The dimension bookkeeping KRS never states explicitly, but which their own
displayed identity forces:
    dim = sum_j (k_j + 2) - (s - 1) = sum_j k_j + s + 1,
and  3 - b_s - k_s eps = eps(3l - m - sum k_i) = (m-l)/l  forces
    sum k_i = 3l - m - 1,   hence   dim = (3l-m-1) + (m-l) + 1 = 2l.

This script re-runs that recursion in exact rational arithmetic for EVERY
m/l in (3/2, 2) with l <= 179 and checks the three invariants.

stdlib only.  Exit 0 on full pass.  Runtime: ~20 s.
"""

from __future__ import annotations

import sys
from fractions import Fraction as F

FAILURES: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> bool:
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"   {detail}" if detail else ""))
    if not cond:
        FAILURES.append(label)
    return cond


def run(m: int, l: int) -> dict:
    """Execute KRS 2002's Lemma 7 / Theorem 6 construction for alpha = m/l in
    (3/2, 2) and return its dimension bookkeeping."""
    alpha = F(m, l)
    eps = alpha - 1
    s = m - l
    assert F(3, 2) < alpha < 2, (m, l)
    b = alpha
    ks: list[int] = []
    dims: list[int] = []
    r = None
    for j in range(s):
        if not (1 <= b <= alpha):
            return dict(ok=False, why=("b out of range", j, b))
        cand = [k for k in (1, 2, 3) if 0 < 3 - b - k * eps <= eps]
        if not cand:
            return dict(ok=False, why=("no admissible k", j, b))
        k = cand[0]
        ks.append(k)
        dims.append(k + 2)          # Proposition 5 block is (k+2) x (k+2)
        r = 3 - b - k * eps
        b = alpha - r
    total_dim = sum(dims) - (s - 1)  # sewing s blocks: dims add, -1 per join
    return dict(
        ok=True,
        alpha=alpha, eps=eps, s=s, ks=ks,
        sumk=sum(ks), pred_sumk=3 * l - m - 1,
        terminal_residue=r, residue_eq_eps=(r == eps),
        dim=total_dim, two_l=2 * l, dim_ok=(total_dim == 2 * l),
    )


def main() -> int:
    print(__doc__)
    print("=" * 78)
    print("KRS 2002 Theorem 6 construction -- exhaustive dimension audit")
    print("=" * 78)

    bad: list[tuple] = []
    n = 0
    for l in range(2, 180):
        for m in range(1, 2 * l):
            a = F(m, l)
            if F(3, 2) < a < 2 and a.denominator == l:
                res = run(m, l)
                n += 1
                if not (res.get("ok") and res["dim_ok"] and res["residue_eq_eps"]
                        and res["sumk"] == res["pred_sumk"]):
                    bad.append((m, l, res))
    # non-reduced m/l are skipped above (a.denominator == l); count both ways
    n_all = 0
    bad_all: list[tuple] = []
    for l in range(2, 180):
        for m in range(1, 2 * l):
            if F(3, 2) < F(m, l) < 2:
                res = run(m, l)
                n_all += 1
                if not (res.get("ok") and res["dim_ok"] and res["residue_eq_eps"]
                        and res["sumk"] == res["pred_sumk"]):
                    bad_all.append((m, l, res))

    check(f"K1  KRS's construction terminates with a valid k_j in {{1,2,3}} at "
          f"every step and has TOTAL DIMENSION EXACTLY 2l, for every m/l in "
          f"(3/2,2) with l <= 179  ({n_all} cases, {len(bad_all)} failures)",
          len(bad_all) == 0, f"{n} of them in lowest terms")
    check("K2  the step counts obey KRS's own displayed identity "
          "sum_j k_j = 3l - m - 1", len(bad_all) == 0)
    check("K3  the recursion's terminal residue equals eps = alpha - 1 exactly "
          "(the stopping condition KRS uses)", len(bad_all) == 0)

    print()
    print("  samples (alpha, number of sewn blocks s, first k_j's, dimension):")
    for (m, l) in [(7, 4), (5, 3), (13, 8), (19, 12), (97, 55), (179, 100)]:
        if not (F(3, 2) < F(m, l) < 2):
            continue
        r = run(m, l)
        head = r["ks"][:8]
        more = "..." if r["s"] > 8 else ""
        print(f"    alpha = {m}/{l}: s = {r['s']}, k = {head}{more}, "
              f"sum_k = {r['sumk']} (predicted {r['pred_sumk']}), "
              f"dim = {r['dim']} = 2*{l}")

    # =====================================================================
    # K4-K5 -- INDEPENDENT RE-DERIVATION OF THE PAPER'S SECTION 4.2 TABLE
    #          by rational interval arithmetic.  No Q(sqrt5), no Decimal.
    # =====================================================================
    print()
    print("=" * 78)
    print("Section 4.2 table, re-derived over Q by interval arithmetic")
    print("=" * 78)

    # A rational bracket for sqrt5, VERIFIED by exact integer comparison
    # (lo^2 < 5 < hi^2) rather than by any theory of continued fractions.
    hh, kk = 2, 1
    hp, kp = 1, 0
    for _ in range(120):
        hh, hp = 4 * hh + hp, hh
        kk, kp = 4 * kk + kp, kk
    c1, c2 = F(hp, kp), F(hh, kk)
    lo, hi = (c1, c2) if c1 < c2 else (c2, c1)
    bracket_ok = (lo * lo < 5 < hi * hi) and (hi - lo) < F(1, 10 ** 100)
    check(f"K4  rational bracket for sqrt5 verified by exact integer comparison "
          f"lo^2 < 5 < hi^2 (denominators of ~{len(str(kk))} digits)",
          bracket_ok,
          f"width hi - lo < 1e-{len(str((hi - lo).denominator)) - len(str((hi - lo).numerator))}")

    # convergents of sqrt5 and the paper's nine rows
    h_, k_ = [2], [1]
    a, b = 1, 0
    for _ in range(8):
        h_.append(4 * h_[-1] + a)
        k_.append(4 * k_[-1] + b)
        a, b = h_[-2], k_[-2]
    convs = [F(h_[i], k_[i]) for i in range(len(h_))]
    rows = [(F(5, 2), F(2), 2, "0.999223")]
    printed = ["0.957906", "0.974133", "0.973200", "0.973252", "0.973249",
               "0.973249", "0.973249", "0.973249"]
    for i in range(len(convs) - 1):
        x, y = convs[i], convs[i + 1]
        p1, p2 = (x, y) if x > y else (y, x)
        rows.append((p1, p2, max(p1.denominator, p2.denominator), printed[i]))

    def eps_bracket(l1: F, l2: F):
        """[eps_lo, eps_hi] for eps = (l1 - sqrt5)(sqrt5 - l2), from the rational
        bracket lo < sqrt5 < hi.  f(x) = (l1-x)(x-l2) is concave with vertex at
        (l1+l2)/2; we ASSERT the vertex is outside [lo,hi] so that f is monotone
        there, and that both factors are positive throughout."""
        vertex = (l1 + l2) / 2
        assert l1 > hi and l2 < lo, (l1, l2)
        assert vertex < lo or vertex > hi, (l1, l2, vertex)
        f_lo = (l1 - lo) * (lo - l2)
        f_hi = (l1 - hi) * (hi - l2)
        return (min(f_lo, f_hi), max(f_lo, f_hi))

    # X = ((2+sqrt5)/(2 sqrt5)) = (5 + 2 sqrt5)/10, so ASY = X^{1/2} and
    # ASY^4 = X^2.  Bracket X, then X^2.
    X_lo, X_hi = (5 + 2 * lo) / 10, (5 + 2 * hi) / 10
    X2_lo, X2_hi = X_lo * X_lo, X_hi * X_hi

    def rel_within(N: int, e_lo: F, e_hi: F, t: F) -> bool:
        """certify  |N eps^{1/4} / ASY - 1| < t  by integer comparison of
        fourth powers: (1-t)^4 < N^4 eps / X^2 < (1+t)^4."""
        n4 = F(N) ** 4
        return (n4 * e_lo > (1 - t) ** 4 * X2_hi
                and n4 * e_hi < (1 + t) ** 4 * X2_lo)

    ok_rows, ok_tail17, ok_tail1292, discriminates = True, True, True, False
    print(f"    {'lam_1':>16s} {'lam_2':>16s} {'N':>7s} {'printed':>10s} "
          f"{'re-derived to +-1e-6':>22s}")
    print("    " + "-" * 76)
    for l1, l2, N, rp in rows:
        e_lo, e_hi = eps_bracket(l1, l2)
        r_p = F(rp)
        n4 = F(N) ** 4
        row_ok = (n4 * e_lo > (r_p - F(1, 10 ** 6)) ** 4
                  and n4 * e_hi < (r_p + F(1, 10 ** 6)) ** 4)
        ok_rows = ok_rows and row_ok
        if N >= 17:
            ok_tail17 = ok_tail17 and rel_within(N, e_lo, e_hi, F(5, 10 ** 3))
        if N >= 1292:
            ok_tail1292 = ok_tail1292 and rel_within(N, e_lo, e_hi, F(5, 10 ** 7))
        if N == 305 and not rel_within(N, e_lo, e_hi, F(5, 10 ** 7)):
            discriminates = True
        print(f"    {str(l1):>16s} {str(l2):>16s} {N:>7d} {rp:>10s} "
              f"{'OK' if row_ok else 'MISMATCH':>22s}")
    print("    " + "-" * 76)

    check("K4  all nine rows of the Section 4.2 table re-derived to +-1e-6 from "
          "the rational bracket alone -- no Q(sqrt5), no Decimal, no float",
          ok_rows and bracket_ok)
    check("K5  Theorem B's TWO tolerances, re-derived independently: "
          "|N eps^{1/4}/ASY - 1| < 5e-3 for every N >= 17, and < 5e-7 for every "
          "N >= 1292 -- while N = 305 FAILS the 5e-7 tolerance, so the "
          "six-figure plateau really does begin at N = 1292 and not before",
          ok_tail17 and ok_tail1292 and discriminates)

    print()
    print("  CONSEQUENCE (paper Lemma 4.6).  Combined with the Coxeter dimension")
    print("  maps of KRS 2002 eq. (2.5) -- verified separately in")
    print("  verify_transport_dimension.py -- this gives d_5(p/q) <= 2q on the")
    print("  whole n = 5 continuous spectrum, from PRIMARY text only.  With the")
    print("  trace bound q | d_5(p/q) this pins d_5(p/q) in {q, 2q}.")

    print()
    print("=" * 78)
    if FAILURES:
        for f in FAILURES:
            print("  FAILED: " + f)
        return 1
    print("  all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
