"""Unit tests for the string calculator.

These tests drive the implementation of the `add` function in
``string_calculator.py``.  Each test is written before the corresponding code
is implemented to follow the Test‑Driven Development (TDD) process.
"""

import unittest

from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    """Tests for the `add` function in the string calculator."""

    def test_empty_string_returns_zero(self):
        """An empty input string should return 0."""
        self.assertEqual(add(""), 0)

    def test_single_number_returns_value(self):
        """A single number should be returned as is."""
        self.assertEqual(add("1"), 1)

    def test_two_numbers_comma_delimited(self):
        """Two comma‑separated numbers should return their sum."""
        self.assertEqual(add("1,5"), 6)

    def test_multiple_numbers(self):
        """An arbitrary number of comma‑separated numbers should return their sum."""
        self.assertEqual(add("1,2,3"), 6)

    def test_newlines_between_numbers(self):
        """Newlines can be used in addition to commas to separate numbers."""
        self.assertEqual(add("1\n2,3"), 6)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
