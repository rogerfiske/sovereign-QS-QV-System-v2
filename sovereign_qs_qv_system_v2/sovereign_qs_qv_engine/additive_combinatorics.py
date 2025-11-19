"""Skeleton for additive-combinatorial analysis utilities."""

from typing import Dict

import numpy as np


def compute_event_differences(matrix: np.ndarray) -> np.ndarray:
    """Compute GF(2) differences between consecutive events."""
    num_events, _ = matrix.shape
    if num_events <= 1:
        return np.zeros((0, matrix.shape[1]), dtype=np.uint8)

    diffs = (matrix[1:, :] ^ matrix[:-1, :]).astype(np.uint8)
    return diffs


def basic_pattern_counts(matrix: np.ndarray) -> Dict[str, int]:
    """Compute simple pattern counts as a starting point."""
    total_ones = int(matrix.sum())
    all_zero_rows = int(np.sum(np.all(matrix == 0, axis=1)))
    all_one_rows = int(np.sum(np.all(matrix == 1, axis=1)))

    return {
        "total_ones": total_ones,
        "all_zero_rows": all_zero_rows,
        "all_one_rows": all_one_rows,
    }


# requirements.txt
# numpy==1.26.4
