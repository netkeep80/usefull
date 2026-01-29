"""Tests for validation utilities."""

import unittest
from usefull.validation import is_email, is_url, is_empty


class TestIsEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_email("user@example.com"))

    def test_valid_email_with_subdomain(self):
        self.assertTrue(is_email("user@mail.example.com"))

    def test_valid_email_with_plus(self):
        self.assertTrue(is_email("user+tag@example.com"))

    def test_invalid_no_at(self):
        self.assertFalse(is_email("userexample.com"))

    def test_invalid_no_domain(self):
        self.assertFalse(is_email("user@"))

    def test_invalid_no_tld(self):
        self.assertFalse(is_email("user@example"))


class TestIsUrl(unittest.TestCase):
    def test_https(self):
        self.assertTrue(is_url("https://example.com"))

    def test_http(self):
        self.assertTrue(is_url("http://example.com"))

    def test_with_port(self):
        self.assertTrue(is_url("http://localhost:8080"))

    def test_with_path(self):
        self.assertTrue(is_url("https://example.com/path/to/page"))

    def test_ftp(self):
        self.assertTrue(is_url("ftp://files.example.com"))

    def test_invalid_no_protocol(self):
        self.assertFalse(is_url("example.com"))

    def test_invalid_text(self):
        self.assertFalse(is_url("not a url"))


class TestIsEmpty(unittest.TestCase):
    def test_none(self):
        self.assertTrue(is_empty(None))

    def test_empty_string(self):
        self.assertTrue(is_empty(""))

    def test_whitespace_string(self):
        self.assertTrue(is_empty("   "))

    def test_empty_list(self):
        self.assertTrue(is_empty([]))

    def test_empty_dict(self):
        self.assertTrue(is_empty({}))

    def test_empty_set(self):
        self.assertTrue(is_empty(set()))

    def test_zero_not_empty(self):
        self.assertFalse(is_empty(0))

    def test_non_empty_string(self):
        self.assertFalse(is_empty("hello"))

    def test_non_empty_list(self):
        self.assertFalse(is_empty([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
