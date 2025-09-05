"""
Module containing the String Calculator implementation.

The `add` function takes a string of numbers separated by delimiters and returns
their sum as an integer.  The implementation will be built incrementally using
Test‑Driven Development (TDD).
"""

from typing import List


def add(numbers: str) -> int:
    """Return the sum of the numbers in a delimited string.

    The function accepts a string containing zero or more non‑negative integers
    separated by delimiters.  It returns the arithmetic sum of the numbers in
    the string.  When the input string is empty, the function returns ``0``.

    The implementation will be built incrementally.  At this stage it only
    supports an empty input string.

    :param numbers: A string containing zero or more numbers separated by
        delimiters (commas by default).
    :return: The sum of the numbers in the string.
    """
    # Requirement 1: An empty input string should return 0.
    if numbers == "":
        return 0

    # If the input contains no delimiters (comma or newline), treat it as a single number.
    if "," not in numbers and "\n" not in numbers:
        try:
            return int(numbers)
        except ValueError as exc:
            # If conversion fails, re‑raise as a NotImplementedError for now.
            raise NotImplementedError("Invalid input format") from exc

    # Handle default delimiters (comma or newline).  We will implement custom
    # delimiters in a later step.  Replace newlines with commas and split.
    # Note: additional whitespace characters are not allowed by the kata's
    # specification, so we don't strip the string.
    # Check for custom delimiter syntax and postpone handling.
    if numbers.startswith("//"):
        raise NotImplementedError("Custom delimiters not implemented yet")

    # Replace newline characters with commas to normalize the delimiters.
    normalized = numbers.replace("\n", ",")
    # Split the string by comma to obtain individual number tokens.
    tokens = [token for token in normalized.split(",") if token != ""]
    try:
        # Convert each token to an integer and sum them.
        int_values = [int(token) for token in tokens]
    except ValueError as exc:
        raise NotImplementedError("Invalid number encountered") from exc
    return sum(int_values)
