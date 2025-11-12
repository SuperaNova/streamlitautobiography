"""Utility helpers for loading structured data used across the Streamlit app."""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


_DATA_DIR = Path(__file__).resolve().parents[1] / "data"


@lru_cache(maxsize=None)
def _load_yaml_cached(relative_path: str) -> Any:
    target = _DATA_DIR / relative_path
    if not target.exists():
        raise FileNotFoundError(f"Data file not found: {target}")

    with target.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_yaml(relative_path: str) -> Any:
    """Return a deep-copied object loaded from the YAML file at *relative_path*."""
    return deepcopy(_load_yaml_cached(relative_path))


def data_dir() -> Path:
    """Expose the resolved data directory for assets such as the resume file."""
    return _DATA_DIR
