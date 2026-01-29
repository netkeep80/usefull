"""Tests for collection utilities."""

import unittest
from usefull.collections import flatten, chunk, unique, group_by


class TestFlatten(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])

    def test_depth_limit(self):
        self.assertEqual(flatten([1, [2, [3, [4]]]], depth=1), [1, 2, [3, [4]]])

    def test_empty(self):
        self.assertEqual(flatten([]), [])

    def test_no_nesting(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_strings_not_flattened(self):
        self.assertEqual(flatten(["hello", ["world"]]), ["hello", "world"])


class TestChunk(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(list(chunk([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]])

    def test_exact_division(self):
        self.assertEqual(list(chunk([1, 2, 3, 4], 2)), [[1, 2], [3, 4]])

    def test_empty(self):
        self.assertEqual(list(chunk([], 5)), [])

    def test_large_chunk_size(self):
        self.assertEqual(list(chunk([1, 2], 10)), [[1, 2]])

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            list(chunk([1, 2], 0))


class TestUnique(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(unique([1, 2, 2, 3, 1, 4]), [1, 2, 3, 4])

    def test_string(self):
        self.assertEqual(unique("abracadabra"), ["a", "b", "r", "c", "d"])

    def test_empty(self):
        self.assertEqual(unique([]), [])

    def test_no_duplicates(self):
        self.assertEqual(unique([1, 2, 3]), [1, 2, 3])


class TestGroupBy(unittest.TestCase):
    def test_modulo(self):
        result = group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        self.assertEqual(result, {1: [1, 3, 5], 0: [2, 4]})

    def test_first_char(self):
        result = group_by(["apple", "banana", "avocado"], lambda x: x[0])
        self.assertEqual(result, {"a": ["apple", "avocado"], "b": ["banana"]})

    def test_length(self):
        result = group_by(["hi", "hello", "hey"], len)
        self.assertEqual(result, {2: ["hi"], 5: ["hello"], 3: ["hey"]})

    def test_empty(self):
        result = group_by([], lambda x: x)
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
