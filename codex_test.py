#!/usr/bin/env python3
"""
Time to test your debugging skills, Codex!
This script has multiple bugs. Can you:
1. Find all the bugs
2. Fix them
3. Add a comment explaining what each bug was
"""

def calculate_average(numbers):
    """Return the average of ``numbers``.

    Bug fix: dividing by ``len(numbers)`` when the list is empty causes a
    ``ZeroDivisionError``. Handle the empty input by returning ``0``.
    """
    total = 0
    for num in numbers:
        total += num
    if not numbers:
        return 0
    return total / len(numbers)

def find_maximum(items):
    """Return the largest value in ``items``.

    Bug fix: ``max_val`` was initialised to ``0`` so lists containing only
    negative numbers would incorrectly return ``0``. Start with the first item
    instead and handle empty lists.
    """
    if not items:
        raise ValueError("items cannot be empty")
    max_val = items[0]
    for item in items[1:]:
        if item > max_val:
            max_val = item
    return max_val

def reverse_string(text):
    """Return ``text`` reversed.

    Bug fix: the function attempted to return ``reverse`` which does not exist.
    Also renamed the accumulator variable to avoid shadowing Python's built-in
    ``reversed``.
    """
    reversed_text = ""
    for i in range(len(text)):
        reversed_text = text[i] + reversed_text
    return reversed_text

if __name__ == "__main__":
    # Test the functions
    # Empty list should now return 0 instead of crashing
    print(calculate_average([]))
    # Should correctly handle negative numbers and return -1
    print(find_maximum([-5, -10, -1]))
    # Should no longer raise a NameError
    print(reverse_string("Codex"))
