"""Numeric manipulation utilities."""

from typing import Union

Number = Union[int, float]


def clamp(value: Number, min_value: Number, max_value: Number) -> Number:
    """
    Constrain a value within a minimum and maximum range.

    Args:
        value: The value to clamp.
        min_value: The minimum allowed value.
        max_value: The maximum allowed value.

    Returns:
        The clamped value.

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(15, 0, 10)
        10
        >>> clamp(3.5, 0.0, 5.0)
        3.5
    """
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    return max(min_value, min(value, max_value))


def lerp(start: Number, end: Number, t: float) -> float:
    """
    Perform linear interpolation between two values.

    Args:
        start: The starting value (returned when t=0).
        end: The ending value (returned when t=1).
        t: The interpolation factor (typically 0 to 1).

    Returns:
        The interpolated value.

    Examples:
        >>> lerp(0, 100, 0.5)
        50.0
        >>> lerp(10, 20, 0.0)
        10.0
        >>> lerp(10, 20, 1.0)
        20.0
        >>> lerp(0, 10, 0.25)
        2.5
    """
    return float(start + (end - start) * t)


def round_to(value: Number, precision: Number) -> float:
    """
    Round a value to an arbitrary precision.

    Args:
        value: The value to round.
        precision: The precision to round to (e.g., 0.5, 10, 0.01).

    Returns:
        The rounded value.

    Examples:
        >>> round_to(7, 5)
        5.0
        >>> round_to(8, 5)
        10.0
        >>> round_to(3.14159, 0.01)
        3.14
        >>> round_to(127, 10)
        130.0
    """
    if precision <= 0:
        raise ValueError("precision must be positive")
    return round(value / precision) * precision


def percentage(value: Number, total: Number) -> float:
    """
    Calculate what percentage a value is of a total.

    Args:
        value: The partial value.
        total: The total value.

    Returns:
        The percentage (0-100 scale).

    Examples:
        >>> percentage(25, 100)
        25.0
        >>> percentage(1, 4)
        25.0
        >>> percentage(0, 100)
        0.0
        >>> percentage(50, 200)
        25.0
    """
    if total == 0:
        raise ValueError("total cannot be zero")
    return float(value / total * 100)
