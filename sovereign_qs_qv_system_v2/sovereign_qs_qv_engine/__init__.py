"""Top-level package for the Sovereign QS/QV engine.

This package contains the foundational building blocks for the
QS/QV Sovereign System v2, including GF(2) canonicalization,
zero quantumization, additive-combinatorial analysis, pattern
lattice construction, exclusionary prediction, and provenance
tracking.

All modules are designed to be mathematically transparent and
compatible with Dr. Elara V. Mercer's sovereignty protocols.
"""

from typing import List

__all__: List[str] = [
    "gf2_canonicalizer",
    "quantumization_operator",
    "additive_combinatorics",
    "pattern_lattice",
    "exclusion_predictor",
    "provenance_layer",
]

# requirements.txt
# numpy==1.26.4
