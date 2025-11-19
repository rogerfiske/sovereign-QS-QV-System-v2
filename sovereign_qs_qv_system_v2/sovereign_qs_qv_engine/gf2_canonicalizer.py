"""GF(2) canonicalization utilities for QS/QV event data.

This module provides functions to:
- Validate QS events (ascending 5-tuples in the range [value_min, value_max]).
- Build a binary presence matrix from QS events.
- Convert existing numeric matrices into GF(2) by reducing values modulo 2.
- Construct complement (hole) matrices where 1 marks absence instead of presence.

All operations are intentionally simple and explicit so that the
human operator can inspect and trust the transformations.
"""

from typing import Iterable, List, Sequence, Tuple

import numpy as np


def validate_qs_events(
    events: Iterable[Sequence[int]],
    value_min: int = 1,
    value_max: int = 39,
    tuple_size: int = 5,
) -> List[Tuple[int, str]]:
    """Validate QS events for ordering and range constraints.

    Args:
        events:
            An iterable of integer sequences, where each sequence represents
            a QS event (e.g., [QS1, QS2, QS3, QS4, QS5]).
        value_min:
            Minimum allowed value for any QS entry (inclusive).
        value_max:
            Maximum allowed value for any QS entry (inclusive).
        tuple_size:
            Expected length of each QS tuple (default 5).

    Returns:
        A list of (index, message) pairs describing any issues found.
        The index is the zero-based event index in the input iterable.

    Notes:
        - The function does not raise; it collects errors so the caller
          can decide how strict to be.
        - This is designed to be used early in the pipeline to ensure
          the dataset is well-formed.
    """
    issues: List[Tuple[int, str]] = []
    for idx, ev in enumerate(events):
        if len(ev) != tuple_size:
            issues.append((idx, f"Invalid tuple length: {len(ev)} (expected {tuple_size})"))
            continue

        if any((v < value_min or v > value_max) for v in ev):
            issues.append((idx, f"Value out of range in event: {ev}"))

        if any(ev[i] >= ev[i + 1] for i in range(len(ev) - 1)):
            issues.append((idx, f"Event is not strictly ascending: {ev}"))

        return issues


def build_presence_matrix(
    events: Iterable[Sequence[int]],
    value_min: int = 1,
    value_max: int = 39,
) -> np.ndarray:
    """Build a GF(2) presence matrix from QS events.

    Each event is mapped to a binary vector of length (value_max - value_min + 1),
    where position j is 1 if the corresponding value appears in the event,
    and 0 otherwise.

    Args:
        events:
            An iterable of integer sequences, where each sequence represents
            a QS event (e.g., [QS1, QS2, QS3, QS4, QS5]).
        value_min:
            Minimum value in the domain (inclusive).
        value_max:
            Maximum value in the domain (inclusive).

    Returns:
        A NumPy array of shape (num_events, num_values) with dtype uint8,
        containing only 0 or 1 entries.

    Raises:
        ValueError:
            If any event contains a value outside [value_min, value_max].
    """
    domain_size: int = value_max - value_min + 1
    rows: List[np.ndarray] = []

    for ev in events:
        row = np.zeros(domain_size, dtype=np.uint8)
        for v in ev:
            if v < value_min or v > value_max:
                raise ValueError(
                    f"Value {v} out of range [{value_min}, {value_max}] in event {ev}."
                )
            idx: int = v - value_min
            row[idx] = 1
        rows.append(row)

    if not rows:
        return np.zeros((0, domain_size), dtype=np.uint8)

    matrix = np.vstack(rows)
    return matrix


def to_gf2(matrix: np.ndarray) -> np.ndarray:
    """Reduce an integer matrix modulo 2 to obtain a GF(2) matrix.

    Args:
        matrix:
            An integer-valued NumPy array. Values are interpreted as
            belonging to the integers and will be reduced modulo 2.

    Returns:
        A NumPy array with the same shape as ``matrix`` and dtype uint8,
        containing entries in {0, 1}.

    Notes:
        - This function does not assume any particular structure in the
          input; it is a low-level utility.
    """
    result = (matrix.astype(np.int64) % 2).astype(np.uint8)
    return result


def build_complement_matrix(matrix: np.ndarray) -> np.ndarray:
    """Construct a complement (hole) matrix from a GF(2) presence matrix.

    Args:
        matrix:
            A NumPy array with entries in {0, 1}. Typically, this is the
            presence matrix produced by :func:`build_presence_matrix`
            or :func:`to_gf2`.

    Returns:
        A NumPy array of the same shape and dtype uint8, where each entry
        is 1 if the corresponding position was 0 in the input, and 0
        otherwise.

    Raises:
        ValueError:
            If any entry in ``matrix`` is not 0 or 1.
    """
    unique_values = np.unique(matrix)
    if not np.all(np.isin(unique_values, [0, 1])):
        raise ValueError(
            f"build_complement_matrix expects a binary matrix; found values: {unique_values!r}"
        )

    complement = np.ones_like(matrix, dtype=np.uint8) - matrix.astype(np.uint8)
    return complement


# requirements.txt
# numpy==1.26.4
