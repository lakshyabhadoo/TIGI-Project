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

    # Check for custom delimiter syntax at the beginning of the string.  The
    # format is "//<delimiter>\n<numbers>".  The delimiter can be one or more
    # characters.  After extracting the delimiter, we will replace both
    # newlines and the custom delimiter with commas to normalize the string.
    delimiter: str | None = None
    number_part = numbers
    if numbers.startswith("//"):
        newline_index = numbers.find("\n")
        if newline_index == -1:
            raise ValueError("Invalid custom delimiter format: missing newline")
        delimiter = numbers[2:newline_index]
        number_part = numbers[newline_index + 1 :]

    # Determine the delimiters to use for splitting.  By default commas and
    # newlines are supported.  When a custom delimiter is specified, we will
    # treat the custom delimiter in addition to newlines as separators.  The
    # original kata does not explicitly state whether commas should still be
    # accepted when using a custom delimiter.  To keep the implementation
    # simple, we will replace any occurrence of the custom delimiter and
    # newlines with commas and then split on commas.  This means commas will
    # effectively continue to be accepted as a delimiter.
    normalized = number_part
    # Replace newline characters with commas to normalize the delimiters.
    normalized = normalized.replace("\n", ",")
    if delimiter:
        normalized = normalized.replace(delimiter, ",")
    # Split the string by comma to obtain individual number tokens, ignoring
    # consecutive delimiters that would produce empty tokens.
    tokens = [token for token in normalized.split(",") if token != ""]
    try:
        # Convert each token to an integer and sum them.
        int_values = [int(token) for token in tokens]
    except ValueError as exc:
        raise NotImplementedError("Invalid number encountered") from exc
    return sum(int_values)
