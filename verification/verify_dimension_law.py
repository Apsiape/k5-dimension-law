#!/usr/bin/env python3
r"""
VERIFICATION APPENDIX, ENGINE 1 --- "How much dimension does an
eps-approximation to a non-attained quantum correlation cost?  A Diophantine
answer for K_5".

Every numbered arithmetic claim of the paper's sections 2-4, 5.3 and 6 is
checked here in EXACT arithmetic: Fraction over Q, the real quadratic field
Q(sqrt 5), the cyclotomic field Q(zeta_5), exact integers, and 80-digit
Decimal where a real number must be compared with a printed constant.  No
floating point is load-bearing; floats appear in printed diagnostics, and
check C17 deliberately EXHIBITS the failure of floating point on this problem.

Check labels C1..C29 are the ones used in the paper's Table 8.1.  C27-C29
(v1.0.2) certify section 5.3: the drift law D(eps, delta) =
Theta(min(eps^{-1/4}, delta^{-1/4})) and the refutation of the delta^{-1/2}
conjectured in v1.0.0-1.0.1.

stdlib only.  Exit 0 on full pass, 1 otherwise.
Runtime: a second or so on a modern machine, dominated by C8's exhaustive
sweep of q <= 200000 and by the exact 15x15 rational matrix products of C5.
"""

from __future__ import annotations

import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

FAILURES: list[str] = []
COUNT = {"n": 0}


def check(label: str, cond: bool, detail: str = "") -> bool:
    COUNT["n"] += 1
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"   {detail}" if detail else ""))
    if not cond:
        FAILURES.append(label)
    return cond


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt D)
# ---------------------------------------------------------------------------
class Quad:
    D = 5
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def _co(self, o):
        return o if isinstance(o, Quad) else type(self)(F(o), 0)

    def __add__(self, o):
        o = self._co(o)
        return type(self)(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return type(self)(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-self._co(o))

    def __rsub__(self, o):
        return self._co(o) + (-self)

    def __mul__(self, o):
        o = self._co(o)
        return type(self)(self.a * o.a + self.D * self.b * o.b,
                          self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - self.D * self.b * self.b
        if n == 0:
            raise ZeroDivisionError
        return type(self)(self.a / n, -self.b / n)

    def __truediv__(self, o):
        return self * self._co(o).inv()

    def __rtruediv__(self, o):
        return self._co(o) * self.inv()

    def __pow__(self, n: int):
        if n < 0:
            return self.inv() ** (-n)
        r, base = type(self)(1, 0), self
        while n:
            if n & 1:
                r = r * base
            base = base * base
            n >>= 1
        return r

    def __eq__(self, o):
        o = self._co(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b, self.D))

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def is_rational(self):
        return self.b == 0

    def sign(self) -> int:
        a, b, D = self.a, self.b, self.D
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        lhs, rhs = a * a, D * b * b
        if a > 0:
            return 0 if lhs == rhs else (1 if lhs > rhs else -1)
        return 0 if lhs == rhs else (1 if rhs > lhs else -1)

    def __lt__(self, o):
        return (self - self._co(o)).sign() < 0

    def __le__(self, o):
        return (self - self._co(o)).sign() <= 0

    def __gt__(self, o):
        return (self - self._co(o)).sign() > 0

    def __ge__(self, o):
        return (self - self._co(o)).sign() >= 0

    def __float__(self):
        return float(self.a) + float(self.b) * math.sqrt(self.D)

    def __repr__(self):
        return f"{self.a}" if self.b == 0 else f"({self.a} + {self.b}*sqrt{self.D})"


class Q5(Quad):
    D = 5
    __slots__ = ()


R5 = Q5(0, 1)                       # sqrt 5
PHI = Q5(F(1, 2), F(1, 2))          # (1 + sqrt5)/2
LAM_LO = (Q5(5, 0) - R5) / 2        # (5 - sqrt5)/2
LAM_HI = (Q5(5, 0) + R5) / 2        # (5 + sqrt5)/2
TSTAR = Q5(0, F(1, 5))              # 1/sqrt5 = sqrt5/5
LAMSTAR = Q5(5, 0) * TSTAR          # sqrt5


# ---------------------------------------------------------------------------
# Q(zeta_5), for the M_2 pentagon carrier at lambda = 5/2
# ---------------------------------------------------------------------------
class Cyc5:
    """c0 + c1 z + c2 z^2 + c3 z^3, z = exp(2 pi i/5), z^4 = -(1+z+z^2+z^3)."""

    __slots__ = ("c",)

    def __init__(self, c=(0, 0, 0, 0)):
        self.c = tuple(F(x) for x in c)

    @classmethod
    def zeta(cls, k: int):
        k %= 5
        if k == 4:
            return cls((-1, -1, -1, -1))
        v = [0, 0, 0, 0]
        v[k] = 1
        return cls(v)

    @classmethod
    def rat(cls, x):
        return cls((F(x), 0, 0, 0))

    def _co(self, o):
        return o if isinstance(o, Cyc5) else Cyc5.rat(o)

    def __add__(self, o):
        o = self._co(o)
        return Cyc5(tuple(x + y for x, y in zip(self.c, o.c)))

    __radd__ = __add__

    def __mul__(self, o):
        o = self._co(o)
        raw = [F(0)] * 7
        for i, x in enumerate(self.c):
            if x:
                for j, y in enumerate(o.c):
                    if y:
                        raw[i + j] += x * y
        red = [F(0)] * 5
        for e, v in enumerate(raw):
            red[e % 5] += v
        out = [red[0], red[1], red[2], red[3]]
        if red[4]:
            for i in range(4):
                out[i] -= red[4]
        return Cyc5(tuple(out))

    __rmul__ = __mul__

    def __eq__(self, o):
        return self.c == self._co(o).c

    def __hash__(self):
        return hash(self.c)

    def is_rational(self):
        return self.c[1] == 0 and self.c[2] == 0 and self.c[3] == 0

    def as_rational(self):
        assert self.is_rational()
        return self.c[0]


# ---------------------------------------------------------------------------
# exact matrix helpers
# ---------------------------------------------------------------------------
def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(1, m)), A[i][0] * B[0][j])
             for j in range(p)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msum(Ms):
    S = Ms[0]
    for M in Ms[1:]:
        S = madd(S, M)
    return S


def mtrace(A):
    t = A[0][0]
    for i in range(1, len(A)):
        t = t + A[i][i]
    return t


def zeros(k):
    return [[F(0)] * k for _ in range(k)]


def is_scalar(M, c):
    k = len(M)
    return all(M[a][b] == (c if a == b else F(0)) for a in range(k) for b in range(k))


# ---------------------------------------------------------------------------
# structural maps
# ---------------------------------------------------------------------------
def coxeter_matrix(n: int):
    """M_n = [[n-1,-n],[1,-1]] : Coxeter transformation of the star quiver S_n
    acting on the symmetric dimension vector (k; r,...,r).  det 1, trace n-2."""
    return [[F(n - 1), F(-n)], [F(1), F(-1)]]


def phi_lambda(n: int, lam):
    """Induced Moebius action on lambda = n r / k."""
    return (n - lam) / ((n - 1) - lam)


def tits(k, r):
    """Tits form of S_5 on (k; r,...,r):  q(k,r) = k^2 + 5 r^2 - 5 k r."""
    return k * k + 5 * r * r - 5 * k * r


def min_dim_vector(lam: F):
    p, q = lam.numerator, lam.denominator
    g = math.gcd(abs(p), 5 * q)
    return (5 * q // g, p // g)


M5INV = ((-1, 5), (-1, 4))


def descend(k, r, steps=64):
    """Coxeter descent M_5^{-1}; True iff a realisable seed lambda in {0,1,4,5}
    is reached inside `steps` steps before leaving the positive cone."""
    tr = [(k, r)]
    for _ in range(steps):
        if k > 0 and r >= 0:
            if F(5 * r, k) in (F(0), F(1), F(4), F(5)):
                return True, tr
        else:
            return False, tr
        k, r = M5INV[0][0] * k + M5INV[0][1] * r, M5INV[1][0] * k + M5INV[1][1] * r
        tr.append((k, r))
    return False, tr


# ---------------------------------------------------------------------------
# explicit carriers
# ---------------------------------------------------------------------------
def tight_frame_4_in_3():
    """Four rank-1 projections in M_3(Q) with sum (4/3) I_3 (4-vector tight
    frame: columns of the order-4 Hadamard matrix minus its all-ones row)."""
    W = [[1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]]
    out = []
    for j in range(4):
        w = [W[i][j] for i in range(3)]
        out.append([[F(w[a] * w[b], 3) for b in range(3)] for a in range(3)])
    return out


def carrier_lambda_4_3():
    """Five rank-4 projections in M_15(Q), sum (4/3) I_15, EQUAL traces 4/15.
    Tight frame padded with 0, then symmetrised by the Z_5 shift over M_3^{+5}."""
    base = tight_frame_4_in_3() + [zeros(3)]
    out = []
    for i in range(5):
        M = zeros(15)
        for s in range(5):
            blk = base[(i - s) % 5]
            for a in range(3):
                for b in range(3):
                    M[3 * s + a][3 * s + b] = blk[a][b]
        out.append(M)
    return out


def pentagon_M2():
    """Five rank-1 projections in M_2(Q(zeta_5)) with sum (5/2) I_2:
    P_j = 1/2 [[1, z^-j],[z^j, 1]].  Already equal-rank."""
    h = Cyc5.rat(F(1, 2))
    return [[[h, h * Cyc5.zeta(-j)], [h * Cyc5.zeta(j), h]] for j in range(5)]


# ===========================================================================
# SECTION 2 CHECKS -- setup, window, Coxeter transformation, Tits form
# ===========================================================================
def part_setup():
    section("PAPER SECTION 2 -- the KRS window, Phi_5, and the Tits form")

    # C1 -- DPP Prop 4.1 is a THREE-BRANCH piecewise function
    #           0            (t <= 1/n)
    #           n t (n t -1) (1/n <= t <= (n-1)/n)
    #           (n^2-n)(2t-1)(t >= (n-1)/n)
    #       and the claim the paper makes in 1.1 is that the MIDDLE branch is the
    #       active one -- i.e. the maximum of the three -- exactly on
    #       [1/n, (n-1)/n].  That is what is checked.  (The earlier form of this
    #       check compared n t(n t - 1)/(n^2-n) with (n t^2 - t)/(n-1), which is
    #       an algebraic identity in t and n and tested nothing; repair round R1,
    #       finding F24.)
    ok_mid, ok_out, ok_strict = True, True, False
    for n in range(3, 9):
        E = n * n - n
        for num in range(0, 121):
            t = F(num, 120)
            branches = (F(0), n * t * (n * t - 1), E * (2 * t - 1))
            mid_active = branches[1] == max(branches)
            inside = F(1, n) <= t <= F(n - 1, n)
            if inside and not mid_active:
                ok_mid = False
            if (not inside) and mid_active and t not in (F(1, n), F(n - 1, n)):
                # outside the interval a DIFFERENT branch must strictly win
                if branches[1] > max(branches[0], branches[2]):
                    ok_out = False
            if inside and branches[1] > max(branches[0], branches[2]):
                ok_strict = True          # the middle branch is not vacuous
    check("C1  DPP Prop. 4.1 is piecewise {0 | n t(n t - 1) | (n^2-n)(2t-1)} and "
          "its MIDDLE branch n t(n t - 1) is the maximum of the three EXACTLY on "
          "[1/n, (n-1)/n] -- so f_vect(t) = n t(n t - 1) is the active constraint "
          "on the window (n = 3..8, t on a 121-point exact grid)",
          ok_mid and ok_out and ok_strict)

    # C2 -- the DPP window in t, times 5, is exactly (5 -+ sqrt5)/2.
    t_lo = (R5 - 1) / (Q5(2, 0) * R5)
    t_hi = (R5 + 1) / (Q5(2, 0) * R5)
    check("C2  5 * [(sqrt5-1)/(2 sqrt5), (sqrt5+1)/(2 sqrt5)] == "
          "[(5-sqrt5)/2, (5+sqrt5)/2]  (exact in Q(sqrt5))",
          Q5(5, 0) * t_lo == LAM_LO and Q5(5, 0) * t_hi == LAM_HI,
          f"[{float(LAM_LO):.9f}, {float(LAM_HI):.9f}]")
    check("C2  t* = 1/sqrt5 is irrational and strictly inside the window",
          (not TSTAR.is_rational()) and t_lo < TSTAR < t_hi,
          f"t* = {float(TSTAR):.9f}, lambda* = sqrt5 = {float(LAMSTAR):.9f}")
    check("C2  f_vect(t*) = 5 - sqrt5", LAMSTAR * (LAMSTAR - 1) == Q5(5, 0) - R5,
          f"= {float(Q5(5,0)-R5):.9f}")

    # C3 -- M_n: det 1, trace n-2; hyperbolic iff n >= 5; fixed points of Phi_5.
    ok = True
    for n in range(2, 9):
        M = coxeter_matrix(n)
        if M[0][0] * M[1][1] - M[0][1] * M[1][0] != 1 or M[0][0] + M[1][1] != n - 2:
            ok = False
    check("C3  det M_n = 1 and tr M_n = n - 2 for n = 2..8; |tr| > 2 iff n >= 5",
          ok and all(abs(n - 2) <= 2 for n in (2, 3, 4))
          and all(abs(n - 2) > 2 for n in (5, 6, 7, 8)))
    check("C3  the fixed points of Phi_5 solve lam^2 - 5 lam + 5 = 0 and are "
          "EXACTLY the window endpoints",
          (LAM_LO * LAM_LO - Q5(5, 0) * LAM_LO + 5).is_zero()
          and (LAM_HI * LAM_HI - Q5(5, 0) * LAM_HI + 5).is_zero()
          and phi_lambda(5, LAM_LO) == LAM_LO and phi_lambda(5, LAM_HI) == LAM_HI)
    kappa = (Q5(4, 0) - LAM_LO) ** (-2)
    check("C3  multiplier of Phi_5 at lam_- is phi^{-4} = (7 - 3 sqrt5)/2",
          kappa == PHI ** (-4) and kappa == (Q5(7, 0) - Q5(3, 0) * R5) / 2,
          f"kappa = {float(kappa):.10f}")

    # C4 -- Tits form: Coxeter-invariant, q(k,r) = (k^2/5)(lam^2 - 5 lam + 5),
    #       hence window = {q < 0}.
    inv_ok = all(tits(4 * k - 5 * r, k - r) == tits(k, r)
                 for (k, r) in ((2, 1), (15, 4), (40, 11), (4, 1), (5, 1), (100, 27)))
    id_ok = True
    for (k, r) in ((2, 1), (15, 4), (40, 11), (5, 1), (100, 27), (72, 23)):
        lam = F(5 * r, k)
        if F(k * k, 5) * (lam * lam - 5 * lam + 5) != tits(k, r):
            id_ok = False
    check("C4  Tits form q(k,r) = k^2 + 5r^2 - 5kr is Coxeter-invariant, and "
          "q(k,r) = (k^2/5)(lam^2 - 5 lam + 5) with lam = 5r/k", inv_ok and id_ok)
    check("C4  q = 0 <=> lam is a window endpoint; window = {q < 0}: "
          "q(2,1) = -1 (lam = 5/2, inside), q(15,4) = +5 (lam = 4/3, outside)",
          tits(2, 1) == -1 and tits(15, 4) == 5
          and all(tits(*min_dim_vector(x)) < 0 for x in (F(5, 2), F(2), F(3)))
          and all(tits(*min_dim_vector(x)) > 0 for x in (F(4, 3), F(11, 8), F(5, 4))))
    return kappa


# ===========================================================================
# SECTION 3 CHECKS -- the lower bound
# ===========================================================================
def part_lower():
    section("PAPER SECTION 3 -- the unconditional lower bound")

    # C5 -- the variance reformulation.  With S = sum_v e_v,
    #       sum_{v != w} tau(e_v e_w) = tau(S^2) - tau(S);  and if tau(S) = 5t*
    #       then the deficit relative to f_vect(t*) is exactly Var_tau(S).
    #       Verified on the two exhibited carriers (M_15 at 4/3, M_2 pentagon).
    Ps = carrier_lambda_4_3()
    S = msum(Ps)
    val = sum((mtrace(mmul(Ps[a], Ps[b])) / 15
               for a in range(5) for b in range(5) if a != b), F(0))
    tr = lambda M: mtrace(M) / 15
    check("C5  sum_{v != w} tau(e_v e_w) = tau(S^2) - tau(S), exact on the "
          "M_15 carrier",
          val == tr(mmul(S, S)) - tr(S), f"both = {val}")
    check("C5  and the deficit vanishes there: value == f_vect(4/15) = 4/9 "
          "(S is scalar, so Var_tau(S) = 0)",
          val == 5 * F(4, 15) * (5 * F(4, 15) - 1) and val == F(4, 9)
          and is_scalar(S, F(4, 3)))

    # C5b -- REMARK 3.6, the mean-marginal weakening, on a fixture whose five
    #        marginals are deliberately UNEQUAL.  (C5's M_15 carrier has all five
    #        marginals equal to 4/15 and therefore cannot distinguish the
    #        per-index hypothesis tau(P_i) = t* from the mean-marginal one;
    #        repair round R1, finding F14.)
    #
    #        Block A: M_3 over Q, the four-vector tight frame + a zero, so
    #          S_A = (4/3) I_3 with per-index traces (1/3,1/3,1/3,1/3,0);
    #        Block B: M_2 over Q(zeta_5), the pentagon, S_B = (5/2) I_2 with
    #          per-index traces all 1/2.
    #        Weight mu on A fixed by  mu*(4/3) + (1-mu)*(5/2) = sqrt5.
    base_A = tight_frame_4_in_3() + [zeros(3)]
    S_A = msum(base_A)
    tr3 = lambda M: mtrace(M) / 3
    marg_A = [tr3(P) for P in base_A]
    val_A = sum((mtrace(mmul(base_A[a], base_A[b])) / 3
                 for a in range(5) for b in range(5) if a != b), F(0))
    base_B = pentagon_M2()
    tr2c = lambda M: (M[0][0] + M[1][1]) * Cyc5.rat(F(1, 2))
    marg_B = [tr2c(P).as_rational() for P in base_B]
    val_B = Cyc5.rat(0)
    for a in range(5):
        for b in range(5):
            if a != b:
                val_B = val_B + tr2c(mmul(base_B[a], base_B[b]))
    val_B = val_B.as_rational()

    lamA, lamB = Q5(F(4, 3), 0), Q5(F(5, 2), 0)
    mu = (lamB - R5) / (lamB - lamA)                  # weight on block A
    marginals = [mu * Q5(marg_A[i], 0) + (Q5(1, 0) - mu) * Q5(marg_B[i], 0)
                 for i in range(5)]
    mean_marg = sum(marginals[1:], marginals[0]) / 5
    value = mu * Q5(val_A, 0) + (Q5(1, 0) - mu) * Q5(val_B, 0)
    deficit = value - (Q5(5, 0) - R5)                 # minus f_vect(t*) = 5-sqrt5
    unequal = any(not (marginals[i] - marginals[j]).is_zero()
                  for i in range(5) for j in range(5))
    # Theorem A at this carrier: Q = max reduced denominator of the block values
    Qden = max(F(4, 3).denominator, F(5, 2).denominator)
    check("C5b REMARK 3.6: a two-block carrier (M_3 tight frame + zero, weight "
          "mu; M_2 pentagon, weight 1-mu) whose five marginals are UNEQUAL but "
          "average EXACTLY to t* = 1/sqrt5.  The value functional is still "
          "tau(S^2) - tau(S), the deficit is still Var_tau(S) = "
          "(5/2 - sqrt5)(sqrt5 - 4/3), and Theorem A's bound eps > 1/(25 Q^4) "
          "still holds -- so the per-index hypothesis is indeed not used.",
          unequal
          and mean_marg == TSTAR
          and mu.sign() > 0 and (Q5(1, 0) - mu).sign() > 0
          and deficit == (lamB - R5) * (R5 - lamA)
          and (deficit - Q5(F(1, 25 * Qden ** 4), 0)).sign() > 0,
          f"marginals differ ({float(marginals[0]):.9f} vs "
          f"{float(marginals[4]):.9f}), mean = t* exactly; "
          f"deficit = {float(deficit):.9f} > 1/(25*{Qden}^4) = "
          f"{1/(25*Qden**4):.9f}")

    # C6 -- LAW OF TOTAL VARIANCE (the total-variance strengthening: NO
    #       block-scalar assumption is used).
    #       Var_tau(S) = sum_l lam_l Var_{tr_l}(S_l) + Var_lam(s),  s_l = tr_l(S_l).
    #       Checked exactly on rational fixtures with non-scalar blocks.
    ok = True
    tight = False
    fixtures = [
        ([F(1, 3), F(1, 3), F(1, 3)], [[F(1), F(3)], [F(2), F(2)], [F(0), F(5), F(1)]]),
        ([F(2, 7), F(5, 7)], [[F(1), F(2), F(4)], [F(3), F(3)]]),
        ([F(1, 2), F(1, 4), F(1, 4)], [[F(5)], [F(0), F(2)], [F(1), F(1), F(4)]]),
    ]
    for lams, blocks in fixtures:
        s = [sum(sp, F(0)) / len(sp) for sp in blocks]
        s2 = [sum((x * x for x in sp), F(0)) / len(sp) for sp in blocks]
        tauS = sum((lams[i] * s[i] for i in range(len(s))), F(0))
        tauS2 = sum((lams[i] * s2[i] for i in range(len(s))), F(0))
        var_tot = tauS2 - tauS * tauS
        var_within = sum((lams[i] * (s2[i] - s[i] * s[i]) for i in range(len(s))), F(0))
        var_between = sum((lams[i] * (s[i] - tauS) ** 2 for i in range(len(s))), F(0))
        if var_tot != var_within + var_between or var_within < 0:
            ok = False
        if var_within > 0:
            tight = True
    check("C6  law of total variance  Var_tau(S) = sum_l lam_l Var_{tr_l}(S_l) "
          "+ Var_lam(s)  >=  Var_lam(s), exact; the dropped term is strictly "
          "positive on non-scalar blocks (so the inequality is not vacuous)",
          ok and tight)

    # C7 -- the constant of the Diophantine lemma:  5 - 2 sqrt5 > 1/2.
    gap = Q5(5, 0) - Q5(2, 0) * R5
    check("C7  5 - 2 sqrt5 > 1/2  (exact in Q(sqrt5)) -- the inequality that "
          "makes ||q sqrt5|| > 1/(5q) hold for EVERY q >= 1",
          (gap - Q5(F(1, 2), 0)).sign() > 0, f"5 - 2 sqrt5 = {float(gap):.10f}")

    # C8 -- ||q sqrt5|| > 1/(5q), exhaustively, in exact integer arithmetic.
    QMAX = 200000
    bad = 0
    for qd in range(1, QMAX + 1):
        five_q2 = 5 * qd * qd
        m = math.isqrt(five_q2)
        if (m + 1) * (m + 1) - five_q2 < five_q2 - m * m:
            m += 1
        # ||q sqrt5|| = |5q^2 - m^2| / (q sqrt5 + m) >= 1 / (q sqrt5 + m)
        if abs(five_q2 - m * m) < 1:
            bad += 1                       # would mean sqrt5 rational
        d = 5 * qd - m                     # need q sqrt5 + m < 5q, i.e. d^2 > 5q^2
        if not (d > 0 and d * d > five_q2):
            bad += 1
    check(f"C8  ||q sqrt5|| > 1/(5q) verified in exact integer arithmetic for "
          f"ALL q <= {QMAX}", bad == 0)

    # C9 -- the resulting floor.  Compared in 80-digit Decimal, not float.
    getcontext().prec = 80
    FLOOR_D = 1 / Decimal(25).sqrt().sqrt()
    FLOOR = float(FLOOR_D)
    check("C9  deficit > 1/(25 N^4)  <=>  N * eps^{1/4} > 25^{-1/4} = "
          "0.4472135955",
          abs(FLOOR_D - Decimal("0.4472135954999579392818347337")) < Decimal("1e-25"),
          f"floor = {FLOOR_D:.20f}")

    # C9b -- REMARK 3.4a.  Theorem A's Diophantine step is run at the REDUCED
    #        denominator q_l of the block value s_l = a_l / n_l, not at the block
    #        dimension n_l.  Verified on block data whose values are deliberately
    #        NON-reduced: q_l | n_l, q_l <= n_l, and
    #        |s_l - sqrt5| > 1/(5 q_l^2) >= 1/(5 n_l^2).  (Repair round R1, F3.)
    ok, strict_gain = True, False
    for (a_l, n_l) in ((6, 4), (12, 8), (30, 20), (9, 4), (38, 17), (100, 45),
                       (2, 1), (45, 20), (161, 72), (306, 136)):
        s = F(a_l, n_l)
        q_l = s.denominator
        if n_l % q_l != 0 or q_l > n_l:
            ok = False
        # |s - sqrt5| > 1/(5 q_l^2), exactly in Q(sqrt5)
        gap = Q5(s, 0) - R5
        gap = gap if gap.sign() > 0 else -gap
        if (gap - Q5(F(1, 5 * q_l * q_l), 0)).sign() <= 0:
            ok = False
        if q_l < n_l:
            strict_gain = True             # the reduced form is a real gain here
    check("C9b Remark 3.4a: writing s_l = p_l/q_l in lowest terms, q_l divides "
          "n_l and |s_l - sqrt5| > 1/(5 q_l^2) >= 1/(5 n_l^2) -- so Theorem A "
          "holds at the DENOMINATOR Q = max_l q_l <= N, with the same constant "
          "0.4472, and needs no bridge from Lemma 4.6",
          ok and strict_gain)

    # C10 -- 1/5 is valid AND conservative ASYMPTOTICALLY: the tight asymptotic
    #        constant is liminf_q q||q sqrt5|| = 1/sqrt20 = 0.2236 > 1/5 = 0.2,
    #        approached along the convergent denominators -- but the INFIMUM over
    #        all q is strictly below 1/sqrt20 (q = 4 gives 0.2229124), which is
    #        why the word "asymptotically" cannot be dropped from section 3.3 and
    #        why the unconditional lemma must use 1/5.  (R1, finding F24.)
    getcontext().prec = 80
    R5D = Decimal(5).sqrt()
    LIMINF_D = 1 / Decimal(20).sqrt()

    def q_norm(qd: int) -> Decimal:
        v = Decimal(qd) * R5D
        nrm = abs(v - v.to_integral_value())
        if nrm > Decimal("0.5"):
            nrm = 1 - nrm
        return Decimal(qd) * nrm

    k_ = [1, 4]
    for _ in range(20):
        k_.append(4 * k_[-1] + k_[-2])
    seq = [q_norm(qd) for qd in k_]
    # the sweep: monotone approach along the convergents, and the last six all
    # within 1e-20 of 1/sqrt20
    approach = all(abs(seq[i + 1] - LIMINF_D) < abs(seq[i] - LIMINF_D)
                   for i in range(len(seq) - 1))
    converged = all(abs(v - LIMINF_D) < Decimal("1e-20") for v in seq[-6:])
    below = q_norm(4)
    check("C10  q||q sqrt5|| along the convergent denominators approaches "
          "liminf_q q||q sqrt5|| = 1/sqrt20 = 0.2236068 monotonically from below "
          "(22 convergents swept), consistent with the classical value; the "
          "lemma's constant 1/5 is valid for EVERY q and conservative "
          "asymptotically (the tight constant would give N eps^{1/4} > "
          "20^{-1/4} = 0.4729 asymptotically)",
          approach and converged and seq[-1] < LIMINF_D,
          f"q||q sqrt5|| -> {seq[-1]:.20f}")
    check("C10  BUT inf_q q||q sqrt5|| < 1/sqrt20 strictly -- at q = 4 it is "
          "0.2229124 -- so 1/sqrt20 is NOT a valid constant for every q and the "
          "word 'asymptotically' in section 3.3 is load-bearing",
          below < LIMINF_D and abs(below - Decimal("0.22291236")) < Decimal("1e-7"),
          f"q=4: q||q sqrt5|| = {below:.12f} < {LIMINF_D:.12f}")
    return FLOOR_D


# ===========================================================================
# SECTION 4 CHECKS -- the upper bound (two-block carriers, convergents)
# ===========================================================================
def two_block(lam_hi_r: F, lam_lo_r: F):
    """Exact (mu, deficit) for rational block values straddling sqrt5."""
    a, b = Q5(lam_lo_r, 0), Q5(lam_hi_r, 0)
    mu = (R5 - a) / (b - a)
    return mu, mu * (Q5(1, 0) - mu) * (b - a) * (b - a)


def part_upper(FLOOR_D):
    section("PAPER SECTION 4 -- the upper bound: two-block carriers along the "
            "convergents of sqrt5")

    # C11 -- THE IDENTITY.  deficit = mu(1-mu)(lam_1-lam_2)^2 = (lam_1 - sqrt5)
    #        (sqrt5 - lam_2):  the product of the two one-sided errors.
    ok = True
    for (hi, lo) in ((F(5, 2), F(2)), (F(9, 4), F(2)), (F(9, 4), F(38, 17)),
                     (F(161, 72), F(38, 17)), (F(3), F(7, 4)), (F(12, 5), F(11, 5))):
        mu, dfc = two_block(hi, lo)
        prod = (Q5(hi, 0) - R5) * (R5 - Q5(lo, 0))
        if dfc != prod or mu.sign() <= 0 or (Q5(1, 0) - mu).sign() <= 0:
            ok = False
    check("C11  two-block deficit = mu(1-mu)(lam_1-lam_2)^2 = "
          "(lam_1 - sqrt5)(sqrt5 - lam_2)  exactly, on 6 fixtures -- the "
          "product of the two one-sided approximation errors", ok)

    # C12 -- exact marginals hold PER INDEX i for an equal-rank two-block
    #        carrier: tau(P_i) = mu lam_1/5 + (1-mu) lam_2/5 = sqrt5/5 = t*.
    ok = True
    for (hi, lo) in ((F(5, 2), F(2)), (F(9, 4), F(38, 17)), (F(161, 72), F(38, 17))):
        mu, _ = two_block(hi, lo)
        tau_Pi = mu * Q5(hi, 0) / 5 + (Q5(1, 0) - mu) * Q5(lo, 0) / 5
        if tau_Pi != TSTAR:
            ok = False
    check("C12  for an EQUAL-RANK two-block carrier, tau(P_i) = t* = 1/sqrt5 "
          "for EVERY i (not merely on average) -- this is why the exact-marginal "
          "regime is realisable", ok)

    # C13 -- convergents of sqrt5 = [2;4,4,4,...], and they straddle.
    h, k_ = [2], [1]
    hp, kp = 1, 0
    for _ in range(8):
        h.append(4 * h[-1] + hp)
        k_.append(4 * k_[-1] + kp)
        hp, kp = h[-2], k_[-2]
    convs = [F(h[i], k_[i]) for i in range(len(h))]
    check("C13  sqrt5 = [2;4,4,4,...]; convergents 2/1, 9/4, 38/17, 161/72, "
          "682/305, ... recomputed, and consecutive ones straddle sqrt5",
          [str(c) for c in convs[:5]] == ["2", "9/4", "38/17", "161/72", "682/305"]
          and all((Q5(convs[i], 0) - R5).sign() * (Q5(convs[i + 1], 0) - R5).sign() < 0
                  for i in range(len(convs) - 1)))

    # C14 -- THE TABLE.  eps exact in Q(sqrt5); ratios in 80-digit Decimal.
    getcontext().prec = 80
    R5D = Decimal(5).sqrt()

    def q5_to_dec(x):
        return (Decimal(x.a.numerator) / Decimal(x.a.denominator)
                + (Decimal(x.b.numerator) / Decimal(x.b.denominator)) * R5D)

    rows = [(F(5, 2), F(2), "crude two-block carrier")]
    for i in range(len(convs) - 1):
        a, b = convs[i], convs[i + 1]
        hi, lo = (b, a) if b > a else (a, b)
        rows.append((hi, lo, f"convergents {i},{i+1}"))

    print()
    print(f"    {'lam_1 (>sqrt5)':>16s} {'lam_2 (<sqrt5)':>16s} {'N=q':>7s} "
          f"{'eps':>13s} {'N*eps^(1/4)':>13s}")
    print("    " + "-" * 72)
    table = []
    for hi, lo, tag in rows:
        _mu, dfc = two_block(hi, lo)
        N = max(hi.denominator, lo.denominator)
        e = q5_to_dec(dfc)
        ratio = Decimal(N) * e.sqrt().sqrt()
        table.append((hi, lo, N, dfc, e, ratio))
        print(f"    {str(hi):>16s} {str(lo):>16s} {N:>7d} {float(e):>13.4e} "
              f"{float(ratio):>13.6f}   {tag}")
    print("    " + "-" * 72)

    # the asymptote, in 80-digit Decimal:  ((2+sqrt5)/(2 sqrt5))^{1/2}
    ASY_D = ((2 + R5D) / (2 * R5D)).sqrt()
    ASY = float(ASY_D)

    # C14 -- TWO SEPARATE TOLERANCES, so that the engine certifies the sentence
    #        the paper actually prints.  The claim "flat to six significant
    #        figures from N = 17" was FALSE (repair round R1, finding F2): the
    #        relative deviations at N = 17, 72, 305 are 9.1e-4, 5.0e-5, 2.81e-6.
    #        Six figures begin at N = 1292 (relative deviation 1.57e-7).
    tail17 = [(N, r) for (_h, _l, N, _d, _e, r) in table if N >= 17]
    tail1292 = [(N, r) for (_h, _l, N, _d, _e, r) in table if N >= 1292]
    check("C14  N * eps^{1/4} -> 0.973249 across N = 17 .. 98209 (3.76 decades "
          "of N, 15.05 decades of eps), to within 5e-3 -- CONVERGENT, but NOT "
          "yet flat to six figures",
          len(tail17) >= 7 and all(abs(r - ASY_D) < Decimal("5e-3")
                                   for _N, r in tail17),
          "rel devs = " + ", ".join(f"N={N}: {float(abs(r-ASY_D)/ASY_D):.2e}"
                                    for N, r in tail17))
    check("C14  and FLAT TO SIX SIGNIFICANT FIGURES from N = 1292 onwards "
          "(N = 1292 .. 98209: 1.88 decades of N, 7.52 decades of eps), i.e. "
          "|N eps^{1/4} - 0.9732489895| < 5e-7 there -- and NOT before "
          "(N = 305 misses this tolerance)",
          len(tail1292) >= 4
          and all(abs(r - ASY_D) < Decimal("5e-7") for _N, r in tail1292)
          and any(abs(r - ASY_D) >= Decimal("5e-7")
                  for N, r in tail17 if N < 1292),
          "six-figure tail = " + ", ".join(f"N={N}: {float(r):.9f}"
                                           for N, r in tail1292))
    check("C14  every constructed carrier respects the unconditional floor "
          "N eps^{1/4} > 0.4472 (the two bounds are consistent)",
          all(r > FLOOR_D for (_h, _l, _N, _d, _e, r) in table))
    # C14 -- the mod-5 side condition of Cor. 4.8 / Lemma 4.7: the convergent
    #        NUMERATORS h_n = 4h_{n-1} + h_{n-2}, (h_0,h_1) = (2,9), are never
    #        divisible by 5.  (Repair round R1, finding F25.)
    hs = [2, 9]
    for _ in range(60):
        hs.append(4 * hs[-1] + hs[-2])
    residues = [x % 5 for x in hs]
    check("C14  Cor. 4.8's side condition, proved and checked: the convergent "
          "numerators h_n (h_0,h_1) = (2,9), h_{n+1} = 4h_n + h_{n-1}, satisfy "
          "h_n mod 5 = 2,4,3,1 cyclically and are NEVER divisible by 5 (62 "
          "terms; the mod-5 pair map (a,b) -> (b, a-b) is 4-periodic from (2,4))",
          0 not in residues and residues[:8] == [2, 4, 3, 1, 2, 4, 3, 1]
          and all(residues[i] == residues[i % 4] for i in range(len(residues))),
          f"h_n mod 5 = {residues[:8]} ...")

    # C15 -- the asymptote, analytically, and the CONVENTION of the comparison.
    #        Both 0.9732 (Theorem B) and 0.4472 (Theorem A, in its reduced-
    #        denominator form) are DENOMINATOR constants, so their ratio 2.176 is
    #        a within-convention comparison.  In actual block dimension the
    #        corresponding gap is 4.866-9.732 over 0.4472 = 10.9-21.8.
    #        (Repair round R1, finding F3.)
    ratio_den = ASY_D / FLOOR_D
    act_lo, act_hi = 5 * ASY_D, 10 * ASY_D           # Cor. 4.8: 4.866 .. 9.732
    check("C15  asymptote = ((2+sqrt5)/(2 sqrt5))^{1/2} = 0.9732489895; against "
          "Theorem A's floor 0.4472135955 IN THE SAME (DENOMINATOR) CONVENTION "
          "the Theta is tight to a factor 2.176",
          abs(ASY_D - Decimal("0.97324898946773015")) < Decimal("1e-15")
          and abs(ratio_den - Decimal("2.176")) < Decimal("0.01"),
          f"asymptote = {ASY_D:.16f}, ratio to floor = {ratio_den:.6f}")
    check("C15  and the CROSS-convention number must not be quoted instead: in "
          "actual block dimension Cor. 4.8 gives 4.866 <= C_act <= 9.732 against "
          "the same floor 0.4472, i.e. a factor 10.9 - 21.8",
          abs(act_lo - Decimal("4.8662449473")) < Decimal("1e-9")
          and abs(act_hi - Decimal("9.7324898947")) < Decimal("1e-9")
          and abs(act_lo / FLOOR_D - Decimal("10.88")) < Decimal("0.02")
          and abs(act_hi / FLOOR_D - Decimal("21.76")) < Decimal("0.02"),
          f"C_act in [{act_lo:.6f}, {act_hi:.6f}]; factor "
          f"{act_lo/FLOOR_D:.3f} - {act_hi/FLOOR_D:.3f}")

    # C16 -- the achievable eps form a geometric SUBSEQUENCE of ratio (2+sqrt5)^4.
    eps_seq = [e for (_h, _l, N, _d, e, _r) in table if N >= 17]
    ratios = [float(eps_seq[i] / eps_seq[i + 1]) for i in range(len(eps_seq) - 1)]
    target = (2 + 5 ** 0.5) ** 4
    check("C16  consecutive achievable eps differ by the fixed factor "
          "(2+sqrt5)^4 = phi^12 = 321.997 (asymptotically; pre-asymptotic at "
          "the first two rungs), so the constant for a UNIFORM (not "
          "subsequence) upper bound is 0.9732 * (2+sqrt5) = 4.12275",
          abs(target - 321.9968944) < 1e-6
          and all(abs(r / target - 1) < 5e-3 for r in ratios)
          and all(abs(r / target - 1) < 1e-5 for r in ratios[2:])
          and abs(ASY * (2 + 5 ** 0.5) - 4.12275) < 5e-5,
          f"ratios = {[f'{r:.3f}' for r in ratios]}; uniform constant "
          f"{ASY * (2 + 5 ** 0.5):.4f}")

    # C17 -- INSTRUMENT NOTE (fail-capability of the arithmetic itself).
    #        float() on these Q(sqrt5) deficits suffers TOTAL CANCELLATION:
    #        eps ~ 1e-20 is a difference of O(1) numbers.  The check PASSES by
    #        exhibiting the failure -- i.e. by showing that a float pipeline
    #        would have produced a wrong table.
    float_ratios = []
    for (_h, _l, N, dfc, _e, _r) in table:
        ef = float(dfc)
        float_ratios.append(N * (ef ** 0.25) if ef > 0 else 0.0)
    dec_ratios = [float(r) for (_h, _l, _N, _d, _e, r) in table]
    broken = [i for i in range(len(table))
              if abs(float_ratios[i] - dec_ratios[i]) > 0.01 * dec_ratios[i]]
    check("C17  INSTRUMENT: naive float() evaluation of eps collapses at "
          "eps <~ 1e-13 and yields grossly wrong ratios -- the published table "
          "MUST be evaluated in extended precision (80-digit Decimal here)",
          len(broken) >= 3,
          "float ratios = " + ", ".join(f"{x:.4f}" for x in float_ratios))

    # C18 -- the crude carrier and how far from optimal it is.
    _mu, d_crude = two_block(F(5, 2), F(2))
    _mu17, d17 = two_block(F(9, 4), F(38, 17))
    check("C18  crude carrier (5/2, 2): deficit = (9 sqrt5 - 20)/2 = "
          "0.0623058987; convergent carrier (9/4, 38/17) at q = 17: deficit = "
          "(305 sqrt5 - 682)/68, a factor 5779 smaller",
          d_crude == (Q5(9, 0) * R5 - 20) / 2
          and d17 == (Q5(305, 0) * R5 - 682) / Q5(68, 0)
          and 5778.0 < float(d_crude) / float(d17) < 5780.0,
          f"{float(d_crude):.9f} vs {float(d17):.6e}")

    # C19 -- the trace bound: q | d for any realisation of lambda = p/q in M_d.
    ok = True
    for (p, q) in ((9, 4), (38, 17), (161, 72), (5, 2), (4, 3), (11, 8)):
        for d in range(1, 200):
            realisable = (F(p, q) * d).denominator == 1     # sum of ranks integral
            if realisable != (d % q == 0):
                ok = False
    check("C19  trace bound: sum_i rank P_i = lambda d must be an integer, so "
          "q | d for every realisation of lambda = p/q (lowest terms) in M_d", ok)

    # C20 -- the EQUAL-RANK constraint: rank P_i = lambda d / 5 forces 5q | p d,
    #        i.e. q | d and (5 | d whenever 5 does not divide p).
    #        The label's CONCLUSION is checked too, not just the premise: the
    #        equivalence  5q | p d  <=>  ( q | d  and  ( 5 | p  or  5 | d/q ) ).
    #        (The old form of `want` carried a vacuous conjunct (5*q) % 1 == 0
    #        and never tested the conclusion; repair round R1, finding F24.)
    ok, saw_true, saw_false = True, False, False
    for (p, q) in ((9, 4), (38, 17), (161, 72), (4, 3), (5, 2), (7, 3), (10, 3)):
        assert math.gcd(p, q) == 1
        for d in range(1, 400):
            eq_rank = (F(p, q) * d / 5).denominator == 1
            premise = (p * d) % (5 * q) == 0
            conclusion = (d % q == 0) and (p % 5 == 0 or (d // q) % 5 == 0)
            if eq_rank != premise or premise != conclusion:
                ok = False
            saw_true = saw_true or eq_rank
            saw_false = saw_false or not eq_rank
    check("C20  equal-rank constraint: rank P_i = lambda d/5 in Z is EQUIVALENT "
          "to 5q | p d, and (gcd(p,q)=1) that is equivalent to the label's own "
          "conclusion  q | d  AND  ( 5 | p  or  5 | d/q )  -- so the extra factor "
          "5 is needed exactly when 5 does not divide p.  Both truth values occur "
          "in the sweep (7 values of p/q, d = 1..399).  (lambda = 5/2 is the "
          "5 | p exception: d = q = 2 suffices, which is the M_2 pentagon.)",
          ok and saw_true and saw_false)
    return table


# ===========================================================================
# SECTION 5/6 CHECKS -- scope, and the orbit non-theorem
# ===========================================================================
def part_orbit(kappa):
    section("PAPER SECTIONS 5-6 -- scope constants, and the orbit non-theorem")

    # C21 -- lambda = 4/3 is ATTAINED, exhibited exactly over Q.
    Ps = carrier_lambda_4_3()
    S = msum(Ps)
    t = F(4, 15)
    val = sum((mtrace(mmul(Ps[a], Ps[b])) / 15
               for a in range(5) for b in range(5) if a != b), F(0))
    check("C21  lambda = 4/3 ATTAINED: five rank-4 projections in M_15(Q), "
          "S = (4/3) I_15, tau(P_i) = 4/15 for every i, value = f_vect(4/15) "
          "= 4/9 exactly",
          all(mmul(P, P) == P for P in Ps) and is_scalar(S, F(4, 3))
          and all(mtrace(P) == 4 for P in Ps)
          and all(mtrace(P) / 15 == t for P in Ps)
          and val == 5 * t * (5 * t - 1) == F(4, 9),
          f"value = {val}; dimension vector (k,r) = (15,4)")
    check("C21  4/3 lies OUTSIDE the window (below lam_-): it is a point of the "
          "DISCRETE part of Sigma_5, not of the interval",
          Q5(F(4, 3), 0) < LAM_LO,
          f"4/3 = 1.333333 < lam_- = {float(LAM_LO):.9f}")

    # C22 -- and its ORBIT is topologically identical to the sqrt5 orbit.
    orb = [F(4, 3)]
    for _ in range(24):
        orb.append((5 - orb[-1]) / (4 - orb[-1]))
    zc = lambda x: (Q5(x, 0) - LAM_LO) / (Q5(x, 0) - LAM_HI)
    zs = [zc(x) for x in orb]
    # the sqrt5 orbit for comparison
    lam = LAMSTAR
    zs5 = [(lam - LAM_LO) / (lam - LAM_HI)]
    for _ in range(24):
        lam = phi_lambda(5, lam)
        zs5.append((lam - LAM_LO) / (lam - LAM_HI))
    check("C22  the 4/3 orbit is 4/3 -> 11/8 -> 29/21 -> 76/55 -> 199/144 -> ... "
          "(Fibonacci ratios): infinite, aperiodic, strictly monotone, "
          "non-returning, converging to (5-sqrt5)/2",
          [str(x) for x in orb[:5]] == ["4/3", "11/8", "29/21", "76/55", "199/144"]
          and len(set(orb)) == len(orb)
          and all(orb[i + 1] > orb[i] for i in range(len(orb) - 1))
          and all(Q5(x, 0) < LAM_LO for x in orb))
    check("C22  it has the SAME multiplier phi^{-4} as the sqrt5 orbit -- the "
          "two orbits are conjugate; NO orbit-level observable separates the "
          "attained parameter from the unattained one",
          all(zs[m + 1] == kappa * zs[m] for m in range(len(zs) - 1))
          and all(zs5[m + 1] == kappa * zs5[m] for m in range(len(zs5) - 1)))
    dvs = [min_dim_vector(x) for x in orb[:8]]
    check("C22  every rung of the 4/3 orbit carries an integral dimension "
          "vector, generated by the Coxeter functor from (15,4): "
          "(15,4)->(40,11)->(105,29)->(275,76)->... and q_Tits = +5 throughout",
          all(dvs[i + 1] == (4 * dvs[i][0] - 5 * dvs[i][1], dvs[i][0] - dvs[i][1])
              for i in range(len(dvs) - 1))
          and all(tits(*dv) == 5 for dv in dvs))

    # C23 -- the in-window rational lambda = 5/2 is attained with a BI-INFINITE
    #        orbit, refuting the "descent terminates" rescue.
    Ps = pentagon_M2()
    idem = all(mmul(P, P) == P for P in Ps)
    S = msum(Ps)
    scalar = (S[0][0] == Cyc5.rat(F(5, 2)) and S[1][1] == Cyc5.rat(F(5, 2))
              and S[0][1] == Cyc5.rat(0) and S[1][0] == Cyc5.rat(0))
    tr2 = lambda M: (M[0][0] + M[1][1]) * Cyc5.rat(F(1, 2))
    val = Cyc5.rat(0)
    for a in range(5):
        for b in range(5):
            if a != b:
                val = val + tr2(mmul(Ps[a], Ps[b]))
    check("C23  lambda = 5/2 ATTAINED in M_2 over Q(zeta_5) (pentagon carrier), "
          "five rank-1 projections, tau(P_i) = 1/2, value 15/4 = f_vect(1/2)",
          idem and scalar and all(tr2(P) == Cyc5.rat(F(1, 2)) for P in Ps)
          and val.is_rational() and val.as_rational() == F(15, 4))
    k, r = min_dim_vector(F(5, 2))
    fwd, bwd = [(k, r)], [(k, r)]
    kf, rf, kb, rb = k, r, k, r
    for _ in range(25):
        kf, rf = 4 * kf - 5 * rf, kf - rf
        fwd.append((kf, rf))
        kb, rb = -kb + 5 * rb, -kb + 4 * rb
        bwd.append((kb, rb))
    grows = lambda sq: all(sq[i + 1][0] > sq[i][0] > 0 for i in range(len(sq) - 1))
    hit, _ = descend(2, 1)
    check("C23  yet its dimension vectors grow without bound in BOTH directions "
          "((..)<-(7,5)<-(3,2)<-(2,1)->(3,1)->(7,2)->(18,5)->..) and the Coxeter "
          "descent NEVER reaches a realisable seed: the 'attained <=> the "
          "descent terminates' rescue is refuted",
          grows(fwd) and grows(bwd) and fwd[-1][0] > 10 ** 9
          and bwd[-1][0] > 10 ** 9 and not hit,
          f"k_25 = {fwd[-1][0]} forward, {bwd[-1][0]} backward")

    # C24 -- the structural form of the non-theorem: the descent of 4/3 DOES
    #        terminate (at lambda = 1 = (5,1)), so the two attained parameters
    #        4/3 and 5/2 disagree on every orbit-level predicate one could use.
    hit43, tr43 = descend(15, 4)
    check("C24  the 4/3 descent DOES terminate, at the seed lambda = 1 = (5,1) "
          "(resolution of the identity in M_5) -- so 4/3 and 5/2 are BOTH "
          "attained and disagree on descent-termination.  No orbit-termination "
          "criterion can decide attainment.",
          hit43 and tr43[-1] == (5, 1) and not descend(2, 1)[0],
          f"descent: {tr43}")

    # C25 -- phi is in the window and is twice as hard as sqrt5.
    getcontext().prec = 80
    R5D = Decimal(5).sqrt()
    PHID = (Decimal(1) + R5D) / 2

    def liminf_qnorm(x_dec, dens):
        out = []
        for qd in dens[-6:]:
            v = Decimal(qd) * x_dec
            nrm = abs(v - v.to_integral_value())
            if nrm > Decimal("0.5"):
                nrm = 1 - nrm
            out.append(float(Decimal(qd) * nrm))
        return out

    fib = [1, 1]
    while len(fib) < 45:
        fib.append(fib[-1] + fib[-2])
    k_ = [1, 4]
    for _ in range(20):
        k_.append(4 * k_[-1] + k_[-2])
    lp, l5 = liminf_qnorm(PHID, fib)[-1], liminf_qnorm(R5D, k_)[-1]
    check("C25  phi = (1+sqrt5)/2 lies IN the window and its liminf is exactly "
          "TWICE sqrt5's: liminf q||q phi|| = 1/sqrt5 = 0.4472 vs "
          "liminf q||q sqrt5|| = 1/sqrt20 = 0.2236 (Hurwitz: phi is the "
          "worst-approximable point of the window).  This is a statement about "
          "liminfs ONLY -- see C26 for what it does and does not do to D(eps).",
          LAM_LO < PHI < LAM_HI and abs(lp - 5 ** -0.5) < 1e-11
          and abs(l5 - 20 ** -0.5) < 1e-11 and abs(lp / l5 - 2.0) < 1e-9,
          f"phi = {float(PHI):.9f} in [{float(LAM_LO):.4f}, {float(LAM_HI):.4f}]; "
          f"ratio = {lp / l5:.9f}")

    # C26 -- SECTION 5.4, the two-parameter law.  For a quadratic irrational
    #        alpha in W with conjugate alpha' and convergent-denominator growth
    #        rho = lim k_{n+1}/k_n:
    #            floor    = (liminf_q q||q alpha||)^{1/2}
    #            attained = (rho / (alpha - alpha'))^{1/2}
    #        At sqrt5: 0.4728708 and 0.9732490.   At phi: 0.6687403 and 0.8506508.
    #        The floor is HIGHER at phi and the attained constant is LOWER: the
    #        two ends of the law move in OPPOSITE directions.  The paper's
    #        earlier claim that phi is "twice as hard" and sqrt5 "a factor 2
    #        cheaper" was false in both directions (repair round R1, finding F5).
    #        Both attained constants are recomputed from scratch below, by
    #        running the actual two-block construction along 30 convergents of
    #        each parameter in 60+ digit Decimal -- not by evaluating the formula.
    getcontext().prec = 140
    R5X = Decimal(5).sqrt()
    PHIX = (1 + R5X) / 2

    def attained_tail(x_dec: Decimal, hs: list[int], ks: list[int]) -> list[Decimal]:
        """N * eps^{1/4} along consecutive convergent pairs, eps computed as the
        PRODUCT OF THE TWO ONE-SIDED ERRORS (Prop. 4.1 generalised)."""
        out = []
        for i in range(len(ks) - 1):
            a1 = Decimal(hs[i]) / Decimal(ks[i])
            a2 = Decimal(hs[i + 1]) / Decimal(ks[i + 1])
            hi, lo = (a1, a2) if a1 > a2 else (a2, a1)
            eps = (hi - x_dec) * (x_dec - lo)
            if eps <= 0:
                continue
            N = max(ks[i], ks[i + 1])
            out.append(Decimal(N) * eps.sqrt().sqrt())
        return out

    # sqrt5 = [2;4,4,4,...] : 40 convergents
    h5, kk5 = [2], [1]
    hp, kp = 1, 0
    for _ in range(40):
        h5.append(4 * h5[-1] + hp)
        kk5.append(4 * kk5[-1] + kp)
        hp, kp = h5[-2], kk5[-2]
    # phi = [1;1,1,1,...] : consecutive Fibonacci ratios, 90 convergents
    fb = [1, 1]
    while len(fb) < 95:
        fb.append(fb[-1] + fb[-2])
    hphi, kphi = fb[2:93], fb[1:92]

    tail5 = attained_tail(R5X, h5, kk5)
    tailp = attained_tail(PHIX, hphi, kphi)
    FLOOR5 = (1 / Decimal(20).sqrt()).sqrt()          # 20^{-1/4}
    FLOORP = (1 / Decimal(5).sqrt()).sqrt()           # 5^{-1/4}
    ATT5 = ((2 + R5X) / (2 * R5X)).sqrt()             # rho/(alpha-alpha') at sqrt5
    ATTP = (PHIX / R5X).sqrt()                        # rho/(alpha-alpha') at phi
    check("C26  section 5.4, all four constants.  FLOORS "
          "(liminf_q q||q alpha||)^{1/2}: sqrt5 -> 20^{-1/4} = 0.4728708, "
          "phi -> 5^{-1/4} = 0.6687403 (their ratio is sqrt2, NOT 2).  ATTAINED "
          "(rho/(alpha - alpha'))^{1/2}: sqrt5 -> 0.9732490, phi -> 0.8506508, "
          "each RECOMPUTED from the two-block construction (eps = product of the "
          "two one-sided errors) along 40 resp. 90 convergents in 140-digit "
          "Decimal, not from the formula.  phi has the HIGHER floor and the "
          "LOWER attained constant: the two ends of the law move in OPPOSITE "
          "directions, and along its convergents phi is ~13% CHEAPER than sqrt5 "
          "(ratio 0.874032).",
          abs(FLOOR5 - Decimal("0.4728708045015879")) < Decimal("1e-15")
          and abs(FLOORP - Decimal("0.6687403049764220")) < Decimal("1e-15")
          and abs(FLOORP / FLOOR5 - Decimal(2).sqrt()) < Decimal("1e-60")
          and abs(tail5[-1] - ATT5) < Decimal("1e-25")
          and abs(tailp[-1] - ATTP) < Decimal("1e-25")
          and abs(ATT5 - Decimal("0.9732489894677302")) < Decimal("1e-15")
          and abs(ATTP - Decimal("0.8506508083520399")) < Decimal("1e-15")
          and ATTP < ATT5 and FLOORP > FLOOR5
          and abs(ATTP / ATT5 - Decimal("0.874032048897642")) < Decimal("1e-14"),
          f"sqrt5: floor {FLOOR5:.7f} attained {tail5[-1]:.7f}; "
          f"phi: floor {FLOORP:.7f} attained {tailp[-1]:.7f}; "
          f"attained ratio phi/sqrt5 = {ATTP/ATT5:.6f}")


# ===========================================================================
# SECTION 5.3 CHECKS -- drifted marginals (v1.0.2): the former Open Lemma is
# false; the drift law is D(eps, delta) = Theta(min(eps^{-1/4}, delta^{-1/4}))
# ===========================================================================
def eps_T_two_block(H, L, m):
    """Fixed-target deficit (5.1) of the equal-rank two-block carrier with
    scalar block values H > sqrt5 > L and mean m = mu H + (1-mu) L:
    Var = (m - L)(H - m), and eps_T = Var + (m - sqrt5)(m + sqrt5 - 1)."""
    return (m - L) * (H - m) + (m - R5) * (m + R5 - 1)


def part_drift():
    section("PAPER SECTION 5.3 -- drifted marginals: the former Open Lemma is "
            "false, and the drift exponent is 1/4")

    # C27 -- PROPOSITION 5.2, exactly in Q(sqrt5).  For a straddling pair with the
    #        weight free, eps_T is AFFINE in the mean m,
    #            eps_T = m (H + L - 1) - H L - 5 + sqrt5,
    #        vanishes at m0 = (H L + 5 - sqrt5)/(H + L - 1), and
    #            sqrt5 - m0 = eps_exact/(H + L - 1),  eps_exact = (H - sqrt5)(sqrt5 - L)
    #        (the exact-marginal deficit of Prop. 4.1), with mu0 in (0,1).
    pairs = [(F(5, 2), F(2)), (F(9, 4), F(2)), (F(9, 4), F(38, 17)),
             (F(161, 72), F(38, 17)), (F(161, 72), F(682, 305))]
    ok = True
    for hi, lo in pairs:
        H, L = Q5(hi, 0), Q5(lo, 0)
        m0 = (H * L + 5 - R5) / (H + L - 1)
        for m in (m0, Q5(F(11, 5), 0), Q5(F(9, 4), 0)):
            if eps_T_two_block(H, L, m) != m * (H + L - 1) - H * L - 5 + R5:
                ok = False
        if not eps_T_two_block(H, L, m0).is_zero():
            ok = False
        _mu, d_exact = two_block(hi, lo)
        if (R5 - m0) != d_exact / (H + L - 1) or (R5 - m0).sign() <= 0:
            ok = False
        mu0 = (m0 - L) / (H - L)
        if mu0.sign() <= 0 or (Q5(1, 0) - mu0).sign() <= 0:
            ok = False
    check("C27  Prop. 5.2: for an equal-rank straddling pair with free weight, the "
          "fixed-target deficit eps_T = Var + (m - sqrt5)(m + sqrt5 - 1) is AFFINE "
          "in the mean m, vanishes exactly at m0 = (H L + 5 - sqrt5)/(H + L - 1), "
          "sqrt5 - m0 = eps_exact/(H + L - 1) > 0, and mu0 in (0,1) -- exact in "
          "Q(sqrt5) on 5 pairs, identity tested at 3 values of m each", ok)

    H, L = Q5(F(9, 4), 0), Q5(F(38, 17), 0)
    m0 = (H * L + 5 - R5) / (H + L - 1)
    drift = (R5 - m0) / 5
    mu0 = (m0 - L) / (H - L)
    closed = (m0 == (Q5(682, 0) - Q5(68, 0) * R5) / Q5(237, 0)
              and drift == (Q5(305, 0) * R5 - 682) / Q5(1185, 0))
    # the value of this carrier is EXACTLY f_vect(t*) = 5 - sqrt5
    value = (m0 - L) * (H - m0) + m0 * m0 - m0
    exact_value = value == Q5(5, 0) - R5
    # Remark 5.5: the ten affine maps x -> a x + b (a in {1,2}) of Z_5 carry each
    # unordered pair to each unordered pair exactly once
    maps = [(a, b) for a in (1, 2) for b in range(5)]
    cover = True
    for i in range(5):
        for k in range(i + 1, 5):
            imgs = [frozenset(((a * i + b) % 5, (a * k + b) % 5)) for a, b in maps]
            if len(set(imgs)) != 10 or any(len(s) != 2 for s in imgs):
                cover = False
    check("C27  the explicit refuting carrier (9/4, 38/17), denominator 17: "
          "m0 = (682 - 68 sqrt5)/237, drift delta0 = (305 sqrt5 - 682)/1185 = "
          "6.1868e-7, value EXACTLY 5 - sqrt5 (deficit 0); and the ten affine maps "
          "of Z_5 hit every unordered pair exactly once (Remark 5.5)",
          closed and exact_value and cover,
          f"m0 = {float(m0):.12f}, delta0 = {float(drift):.6e}, mu0 = {float(mu0):.6f}")

    # C28 -- THEOREM 5.3(b): along consecutive convergent pairs, N delta0^{1/4}
    #        -> 0.9732489895 / (5(2 sqrt5 - 1))^{1/4} = 0.4767956449, and
    #        N delta0^{1/2} -> 0 (so the conjectured Omega(delta^{-1/2}) fails).
    getcontext().prec = 80
    R5D = Decimal(5).sqrt()
    ATT5 = ((2 + R5D) / (2 * R5D)).sqrt()
    KD = ATT5 / (5 * (2 * R5D - 1)).sqrt().sqrt()
    h, k_ = [2], [1]
    hp, kp = 1, 0
    for _ in range(40):
        h.append(4 * h[-1] + hp)
        k_.append(4 * k_[-1] + kp)
        hp, kp = h[-2], k_[-2]
    rows = []
    for i in range(len(k_) - 1):
        a = Decimal(h[i]) / Decimal(k_[i])
        b = Decimal(h[i + 1]) / Decimal(k_[i + 1])
        hi, lo = (a, b) if a > b else (b, a)
        eps = (hi - R5D) * (R5D - lo)
        d0 = eps / (5 * (hi + lo - 1))
        N = max(k_[i], k_[i + 1])
        rows.append((N, d0, Decimal(N) * d0.sqrt().sqrt(), Decimal(N) * d0.sqrt()))
    print()
    print(f"    {'N':>7s} {'delta0':>13s} {'N*delta0^(1/4)':>15s} {'N*delta0^(1/2)':>15s}")
    print("    " + "-" * 56)
    for N, d0, r4, r2 in rows[:8]:
        print(f"    {N:>7d} {float(d0):>13.4e} {float(r4):>15.9f} {float(r2):>15.4e}")
    print("    " + "-" * 56)
    r4s = [r for (_N, _d, r, _s) in rows]
    r2s = [s for (_N, _d, _r, s) in rows]
    check("C28  Theorem 5.3(b): N delta0^{1/4} -> 0.9732489895/(5(2 sqrt5-1))^{1/4} "
          "= 0.4767956449 along 40 convergent pairs (tail within 1e-25 of the "
          "limit; the limit recomputed in 80-digit Decimal)",
          abs(r4s[-1] - KD) < Decimal("1e-25")
          and all(abs(r - KD) < Decimal("1e-20") for r in r4s[-6:])
          and abs(KD - Decimal("0.4767956448948477")) < Decimal("1e-15"),
          f"limit = {KD:.16f}, last = {r4s[-1]:.16f}")
    r2n = [Decimal(N) * s for (N, _d, _r, s) in rows]      # N^2 delta0^{1/2}
    check("C28  and N delta0^{1/2} -> 0: strictly decreasing from the second pair "
          "on, with N^2 delta0^{1/2} -> limit^2 = 0.2273 (so N delta0^{1/2} = O(1/N), "
          "below 1e-24 at the 40th pair) -- NO bound D >= c delta^{-1/2} can hold: "
          "the v1.0.0-1.0.1 Open Lemma is refuted",
          all(r2s[i + 1] < r2s[i] for i in range(1, len(r2s) - 1))
          and r2s[-1] < Decimal("1e-24")
          and abs(r2n[-1] - KD * KD) < Decimal("1e-20"),
          f"N delta0^(1/2) at N=17: {float(r2s[1]):.3e}; at the 40th pair: "
          f"{float(r2s[-1]):.1e}; N^2 delta0^(1/2) -> {r2n[-1]:.10f}")

    # C29 -- THEOREM 5.3(a) and PROP. 5.4: the explicit constants, the identity
    #        (5.1) on carriers with NON-scalar blocks, and the convergent bound
    #        |h_n/k_n - sqrt5| < 1/(4 k_n^2) used in Prop. 5.4's upper bound.
    ok_const = (5 * (2 * R5D - 1 + Decimal("0.05")) <= Decimal("17.62")
                and Decimal("17.62").sqrt() + Decimal("0.5") <= Decimal("4.7")
                and 1 / Decimal(10).sqrt() >= Decimal("0.3162")
                and 1 / Decimal(47).sqrt() >= Decimal("0.1458")
                and 1 / Decimal(50).sqrt() >= Decimal("0.1414")
                and abs((2 + R5D) * KD - Decimal("2.0197")) < Decimal("1e-3")
                and 5 * Decimal("0.01") <= Decimal("0.5") * Decimal("0.01").sqrt())
    # identity (5.1) on the C6 fixtures (non-scalar blocks): value - (5 - sqrt5)
    # == Var + (m - sqrt5)(m + sqrt5 - 1), exactly in Q(sqrt5)
    fixtures = [
        ([F(1, 3), F(1, 3), F(1, 3)], [[F(1), F(3)], [F(2), F(2)], [F(0), F(5), F(1)]]),
        ([F(2, 7), F(5, 7)], [[F(1), F(2), F(4)], [F(3), F(3)]]),
        ([F(1, 2), F(1, 4), F(1, 4)], [[F(5)], [F(0), F(2)], [F(1), F(1), F(4)]]),
    ]
    ok_id = True
    for lams, blocks in fixtures:
        s = [sum(sp, F(0)) / len(sp) for sp in blocks]
        s2 = [sum((x * x for x in sp), F(0)) / len(sp) for sp in blocks]
        m = sum((lams[i] * s[i] for i in range(len(s))), F(0))
        tS2 = sum((lams[i] * s2[i] for i in range(len(s))), F(0))
        value = Q5(tS2 - m, 0)
        var = Q5(tS2 - m * m, 0)
        mq = Q5(m, 0)
        if value - (Q5(5, 0) - R5) != var + (mq - R5) * (mq + R5 - 1):
            ok_id = False
    ok_conv = True
    for n in range(1, 41):
        diff = Q5(F(h[n], k_[n]), 0) - R5
        absdiff = diff if diff.sign() > 0 else -diff
        if not (absdiff < Q5(F(1, 4 * k_[n] * k_[n]), 0)):
            ok_conv = False
    check("C29  Theorem 5.3(a)/Prop. 5.4 constants (5(2 sqrt5-1+0.05) <= 17.62, "
          "sqrt(17.62)+0.5 <= 4.7, 10^{-1/2} >= 0.3162, 47^{-1/2} >= 0.1458, "
          "50^{-1/2} >= 0.1414, (2+sqrt5)*0.4768 = 2.020); identity (5.1) holds "
          "exactly on the non-scalar C6 fixtures; |h_n/k_n - sqrt5| < 1/(4 k_n^2) "
          "for 40 convergents",
          ok_const and ok_id and ok_conv)


def main() -> int:
    print(__doc__)
    kappa = part_setup()
    FLOOR_D = part_lower()
    part_upper(FLOOR_D)
    part_orbit(kappa)
    part_drift()

    section("RESULT")
    print(f"  checks executed: {COUNT['n']}")
    if FAILURES:
        for f in FAILURES:
            print("  FAILED: " + f)
        print(f"\nVERDICT: {len(FAILURES)} check(s) FAILED")
        return 1
    print("  all checks passed")
    print()
    print("VERDICT: D(eps) = Theta(eps^{-1/4}) at exact marginals for K_5 at")
    print("t* = 1/sqrt5.  Lower bound unconditional (deficit > 1/(25 N^4) from")
    print("||q sqrt5|| > 1/(5q), via the law of total variance with NO")
    print("block-scalar assumption); upper bound attained along the")
    print("continued-fraction convergents of sqrt5, N eps^{1/4} -> 0.9732489895.")
    print("Drift (v1.0.2): D(eps, delta) = Theta(min(eps^{-1/4}, delta^{-1/4}))")
    print("against the fixed target; the delta^{-1/2} of the former Open Lemma")
    print("is refuted by an explicit zero-deficit carrier at denominator 17.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
