# usefull

A collection of useful utility functions for Python.

## Installation

```bash
pip install .
```

Or install in development mode:

```bash
pip install -e .
```

## Usage

```python
from usefull import slugify, truncate, flatten, chunk, is_email, is_empty, clamp, lerp

# Text utilities
print(slugify("Hello World!"))  # "hello-world"
print(truncate("Long text here", 10))  # "Long te..."
print(word_count("Hello World"))  # 2

# Collection utilities
print(flatten([1, [2, 3], [4, [5]]]))  # [1, 2, 3, 4, 5]
print(list(chunk([1, 2, 3, 4, 5], 2)))  # [[1, 2], [3, 4], [5]]
print(unique([1, 2, 2, 3, 1]))  # [1, 2, 3]

# Validation utilities
print(is_email("user@example.com"))  # True
print(is_url("https://example.com"))  # True
print(is_empty(""))  # True

# Numeric utilities
print(clamp(15, 0, 10))  # 10
print(lerp(0, 100, 0.5))  # 50.0
```

## Available Functions

### Text Utilities (`usefull.text`)

- `slugify(text, separator="-")` - Convert text to URL-friendly slug
- `truncate(text, max_length, suffix="...")` - Truncate text with suffix
- `word_count(text)` - Count words in text
- `remove_duplicates(text, separator=None)` - Remove duplicate words

### Collection Utilities (`usefull.collections`)

- `flatten(nested, depth=-1)` - Flatten nested iterables
- `chunk(iterable, size)` - Split iterable into chunks
- `unique(iterable)` - Get unique elements preserving order
- `group_by(iterable, key)` - Group elements by key function

### Validation Utilities (`usefull.validation`)

- `is_email(value)` - Check if string is valid email format
- `is_url(value)` - Check if string is valid URL format
- `is_empty(value)` - Check if value is empty (None, "", [], {})

### Numeric Utilities (`usefull.numeric`)

- `clamp(value, min_value, max_value)` - Constrain value within a range
- `lerp(start, end, t)` - Linear interpolation between two values
- `round_to(value, precision)` - Round to arbitrary precision
- `percentage(value, total)` - Calculate percentage of a value

## Running Tests

```bash
python -m pytest tests/ -v
```

## Completed Tasks

| Issue | Description | Date |
|-------|-------------|------|
| ISSUE-1 | Set up task tracking system | 2026-01-29 |
| ISSUE-2 | Add useful content to the repository | 2026-01-29 |
| ISSUE-3 | Add numeric utilities module | 2026-01-29 |

## Contributing

1. Check [TASKS.md](TASKS.md) for available tasks
2. Complete a task
3. Update this README.md with the completion
4. Submit a pull request

## License

This project is released into the public domain under the [Unlicense](LICENSE).
