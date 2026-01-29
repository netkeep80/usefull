"""Tests for numeric utilities."""

import unittest
from usefull.numeric import clamp, lerp, round_to, percentage


class TestClamp(unittest.TestCase):
    def test_value_within_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_value_below_min(self):
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_value_above_max(self):
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_float_values(self):
        self.assertEqual(clamp(3.5, 0.0, 5.0), 3.5)

    def test_value_at_min(self):
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_value_at_max(self):
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


class TestLerp(unittest.TestCase):
    def test_midpoint(self):
        self.assertEqual(lerp(0, 100, 0.5), 50.0)

    def test_start(self):
        self.assertEqual(lerp(10, 20, 0.0), 10.0)

    def test_end(self):
        self.assertEqual(lerp(10, 20, 1.0), 20.0)

    def test_quarter(self):
        self.assertEqual(lerp(0, 10, 0.25), 2.5)

    def test_negative_values(self):
        self.assertEqual(lerp(-10, 10, 0.5), 0.0)

    def test_extrapolation_above(self):
        self.assertEqual(lerp(0, 10, 1.5), 15.0)

    def test_extrapolation_below(self):
        self.assertEqual(lerp(0, 10, -0.5), -5.0)


class TestRoundTo(unittest.TestCase):
    def test_round_to_5_down(self):
        self.assertEqual(round_to(7, 5), 5.0)

    def test_round_to_5_up(self):
        self.assertEqual(round_to(8, 5), 10.0)

    def test_round_to_decimal(self):
        self.assertAlmostEqual(round_to(3.14159, 0.01), 3.14, places=2)

    def test_round_to_10(self):
        self.assertEqual(round_to(127, 10), 130.0)

    def test_already_rounded(self):
        self.assertEqual(round_to(10, 5), 10.0)

    def test_invalid_precision(self):
        with self.assertRaises(ValueError):
            round_to(5, 0)

    def test_negative_precision(self):
        with self.assertRaises(ValueError):
            round_to(5, -1)


class TestPercentage(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(percentage(25, 100), 25.0)

    def test_fraction(self):
        self.assertEqual(percentage(1, 4), 25.0)

    def test_zero_value(self):
        self.assertEqual(percentage(0, 100), 0.0)

    def test_half(self):
        self.assertEqual(percentage(50, 200), 25.0)

    def test_full(self):
        self.assertEqual(percentage(100, 100), 100.0)

    def test_over_100(self):
        self.assertEqual(percentage(150, 100), 150.0)

    def test_zero_total(self):
        with self.assertRaises(ValueError):
            percentage(50, 0)


if __name__ == "__main__":
    unittest.main()
