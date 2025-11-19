"""Skeleton for provenance and sovereignty utilities."""

from typing import Dict

import hashlib
from pathlib import Path


def hash_file(path: Path, algorithm: str = "sha256") -> str:
    """Compute a cryptographic hash of a file."""
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        hasher = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def hash_many(paths: Dict[str, Path], algorithm: str = "sha256") -> Dict[str, str]:
    """Hash multiple files and return a mapping of keys to digests."""
    digests: Dict[str, str] = {}
    for key, path in paths.items():
        digests[key] = hash_file(path, algorithm=algorithm)

    return digests


# requirements.txt
# numpy==1.26.4
