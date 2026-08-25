# Release notes — v1.0.1 (2026-08-25)

Priority-section correction release. The theorem, the verification
engines, and all constants are unchanged.

## The correction (paper/PAPER-K5.md, Section 7.2)

The v1.0.0 text stated that the elementary non-closure proof via
embezzlement (Coladangelo, arXiv:1904.02350, Quantum 4, 282) is a nearby
witness "likewise with no rate." **That was wrong.** The paper's abstract
states an explicit dimension lower bound: an epsilon-close to optimal
strategy requires an entangled state of dimension 2^Omega(eps^(-1/8)).
Verified against the primary source 2026-08-24.

The corrected text records: (a) that bound is a dimension *lower* bound
only — no matching upper bound, no explicit near-optimal strategy with
quantified dimension, no tightness claim — so it does not constitute a
two-sided characterization; (b) it is nonetheless prior art for the
existence of a dimension rate attached to a non-closure witness, and the
priority claim is scoped accordingly. The sweep heading is tightened
from "the citing literature contains no rate" to "no rate **for this
witness**."

The priority of D(eps) = Theta(eps^(-1/4)) for the K_5 witness is
unaffected, and its label remains as v1.0.0 stated it: new,
provisional — "no evidence found," not "proved absent."

## Provenance

The error was found during the 2026-08-24/25 cross-repository priority
audit of the I3322 rate claim (see `paper/PRIORITY-AUDIT.md` amendment
in the `i3322-exact-wall` repository), which read the Coladangelo
abstract directly. Corrections of this kind are filed openly; the
correction record is part of the result.
