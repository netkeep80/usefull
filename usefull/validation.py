"""Validation utilities."""

import re
from typing import Any


def is_email(value: str) -> bool:
    """
    Check if a string is a valid email address format.

    Args:
        value: The string to check.

    Returns:
        True if the string looks like a valid email address.

    Examples:
        >>> is_email("user@example.com")
        True
        >>> is_email("invalid-email")
        False
        >>> is_email("user.name+tag@domain.co.uk")
        True
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, value))


def is_url(value: str) -> bool:
    """
    Check if a string is a valid URL format.

    Args:
        value: The string to check.

    Returns:
        True if the string looks like a valid URL.

    Examples:
        >>> is_url("https://example.com")
        True
        >>> is_url("http://localhost:8080/path")
        True
        >>> is_url("not a url")
        False
        >>> is_url("ftp://files.example.com")
        True
    """
    pattern = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, value, re.IGNORECASE))


def is_empty(value: Any) -> bool:
    """
    Check if a value is "empty" (None, empty string, empty collection).

    Args:
        value: The value to check.

    Returns:
        True if the value is considered empty.

    Examples:
        >>> is_empty(None)
        True
        >>> is_empty("")
        True
        >>> is_empty("   ")
        True
        >>> is_empty([])
        True
        >>> is_empty({})
        True
        >>> is_empty(0)
        False
        >>> is_empty("hello")
        False
    """
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) == 0
    return False
