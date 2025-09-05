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

    def test_custom_delimiter(self):
        """A custom delimiter can be specified in the format '//<delim>\n<nums>'"""
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_number_raises_exception(self):
        """Passing a negative number should raise an exception with an informative message."""
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertIn("negative numbers not allowed", str(context.exception))
        self.assertIn("-2", str(context.exception))

    def test_multiple_negative_numbers_raises_exception_with_all_values(self):
        """All negative numbers should be listed in the exception message."""
        with self.assertRaises(ValueError) as context:
            add("-1,-2,3")
        message = str(context.exception)
        # Ensure the base message is present
        self.assertIn("negative numbers not allowed", message)
        # The message should list both negative values separated by a comma
        self.assertIn("-1", message)
        self.assertIn("-2", message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
