"""Tests for text utilities."""

import unittest
from usefull.text import slugify, truncate, word_count, remove_duplicates


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_special_characters(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_custom_separator(self):
        self.assertEqual(slugify("Hello World", "_"), "hello_world")

    def test_multiple_spaces(self):
        self.assertEqual(slugify("Hello    World"), "hello-world")

    def test_unicode(self):
        # Unicode should be normalized to ASCII
        result = slugify("Café")
        self.assertEqual(result, "cafe")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")


class TestTruncate(unittest.TestCase):
    def test_no_truncation_needed(self):
        self.assertEqual(truncate("Hello", 10), "Hello")

    def test_truncation(self):
        self.assertEqual(truncate("Hello World", 8), "Hello...")

    def test_exact_length(self):
        self.assertEqual(truncate("Hello", 5), "Hello")

    def test_custom_suffix(self):
        self.assertEqual(truncate("Hello World", 9, "…"), "Hello Wo…")


class TestWordCount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(word_count("Hello World"), 2)

    def test_multiple_spaces(self):
        self.assertEqual(word_count("  multiple   spaces  "), 2)

    def test_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_single_word(self):
        self.assertEqual(word_count("Hello"), 1)


class TestRemoveDuplicates(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            remove_duplicates("apple banana apple cherry banana"),
            "apple banana cherry"
        )

    def test_custom_separator(self):
        self.assertEqual(remove_duplicates("a,b,a,c", ","), "a,b,c")

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates("a b c"), "a b c")

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates("a a a"), "a")


if __name__ == "__main__":
    unittest.main()
