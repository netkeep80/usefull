"""Collection manipulation utilities."""

from typing import Any, Callable, Dict, Iterable, Iterator, List, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def flatten(nested: Iterable[Any], depth: int = -1) -> List[Any]:
    """
    Flatten a nested iterable structure.

    Args:
        nested: The nested iterable to flatten.
        depth: Maximum depth to flatten (-1 for unlimited).

    Returns:
        A flattened list.

    Examples:
        >>> flatten([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten([1, [2, [3, [4]]]], depth=1)
        [1, 2, [3, [4]]]
        >>> flatten([[1, 2], [3, 4]])
        [1, 2, 3, 4]
    """
    result = []
    for item in nested:
        if depth != 0 and isinstance(item, (list, tuple)) and not isinstance(item, str):
            result.extend(flatten(item, depth - 1 if depth > 0 else -1))
        else:
            result.append(item)
    return result


def chunk(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    """
    Split an iterable into chunks of specified size.

    Args:
        iterable: The iterable to split.
        size: The size of each chunk.

    Yields:
        Lists of items, each with at most 'size' elements.

    Examples:
        >>> list(chunk([1, 2, 3, 4, 5], 2))
        [[1, 2], [3, 4], [5]]
        >>> list(chunk("abcdef", 3))
        [['a', 'b', 'c'], ['d', 'e', 'f']]
        >>> list(chunk([], 5))
        []
    """
    if size <= 0:
        raise ValueError("Chunk size must be positive")

    items = list(iterable)
    for i in range(0, len(items), size):
        yield items[i : i + size]


def unique(iterable: Iterable[T]) -> List[T]:
    """
    Return unique elements from an iterable while preserving order.

    Args:
        iterable: The iterable to process.

    Returns:
        A list with unique elements in original order.

    Examples:
        >>> unique([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
        >>> unique("abracadabra")
        ['a', 'b', 'r', 'c', 'd']
        >>> unique([])
        []
    """
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def group_by(iterable: Iterable[T], key: Callable[[T], K]) -> Dict[K, List[T]]:
    """
    Group elements by a key function.

    Args:
        iterable: The iterable to group.
        key: Function that returns the group key for each element.

    Returns:
        A dictionary mapping keys to lists of elements.

    Examples:
        >>> group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4]}
        >>> group_by(["apple", "banana", "cherry"], lambda x: x[0])
        {'a': ['apple'], 'b': ['banana'], 'c': ['cherry']}
        >>> group_by(["hi", "hello", "hey"], len)
        {2: ['hi'], 5: ['hello'], 3: ['hey']}
    """
    result: Dict[K, List[T]] = {}
    for item in iterable:
        k = key(item)
        if k not in result:
            result[k] = []
        result[k].append(item)
    return result
