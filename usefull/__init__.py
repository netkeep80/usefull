"""
usefull - A collection of useful utility functions.

This package provides commonly needed utility functions for everyday programming tasks.
"""

from usefull.text import (
    slugify,
    truncate,
    word_count,
    remove_duplicates,
)
from usefull.collections import (
    flatten,
    chunk,
    unique,
    group_by,
)
from usefull.validation import (
    is_email,
    is_url,
    is_empty,
)

__version__ = "0.1.0"
__all__ = [
    # Text utilities
    "slugify",
    "truncate",
    "word_count",
    "remove_duplicates",
    # Collection utilities
    "flatten",
    "chunk",
    "unique",
    "group_by",
    # Validation utilities
    "is_email",
    "is_url",
    "is_empty",
]
