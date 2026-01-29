"""Text manipulation utilities."""

import re
import unicodedata
from typing import Optional


def slugify(text: str, separator: str = "-") -> str:
    """
    Convert text to a URL-friendly slug.

    Args:
        text: The text to convert.
        separator: The character to use as word separator (default: "-").

    Returns:
        A lowercase, ASCII-only string with words separated by the separator.

    Examples:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify("Python is Awesome", separator="_")
        'python_is_awesome'
        >>> slugify("Привет мир")
        'privet-mir'
    """
    # Normalize unicode characters to ASCII equivalents
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters with separator
    text = re.sub(r"[^a-z0-9]+", separator, text)
    # Remove leading/trailing separators
    text = text.strip(separator)
    return text


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length, adding a suffix if truncated.

    Args:
        text: The text to truncate.
        max_length: Maximum length of the result (including suffix).
        suffix: String to append when truncating (default: "...").

    Returns:
        The truncated text with suffix if it was shortened.

    Examples:
        >>> truncate("Hello World", 8)
        'Hello...'
        >>> truncate("Hi", 10)
        'Hi'
        >>> truncate("Long text here", 10, suffix="…")
        'Long text…'
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def word_count(text: str) -> int:
    """
    Count the number of words in text.

    Args:
        text: The text to count words in.

    Returns:
        The number of words.

    Examples:
        >>> word_count("Hello World")
        2
        >>> word_count("  multiple   spaces  ")
        2
        >>> word_count("")
        0
    """
    words = text.split()
    return len(words)


def remove_duplicates(text: str, separator: Optional[str] = None) -> str:
    """
    Remove duplicate words or lines from text while preserving order.

    Args:
        text: The text to process.
        separator: Split by this separator (default: None splits by whitespace).

    Returns:
        Text with duplicates removed.

    Examples:
        >>> remove_duplicates("apple banana apple cherry banana")
        'apple banana cherry'
        >>> remove_duplicates("a,b,a,c", separator=",")
        'a,b,c'
    """
    if separator is None:
        parts = text.split()
        join_sep = " "
    else:
        parts = text.split(separator)
        join_sep = separator

    seen = set()
    result = []
    for part in parts:
        if part not in seen:
            seen.add(part)
            result.append(part)
    return join_sep.join(result)
