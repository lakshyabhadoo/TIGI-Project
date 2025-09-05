import unittest

from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    """Tests for the `add` function in the string calculator."""

    def test_empty_string_returns_zero(self):
        """An empty input string should return 0."""
        self.assertEqual(add(""), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

