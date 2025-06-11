#!/usr/bin/env python3
"""
Time to test your debugging skills, Codex!
This script has multiple bugs. Can you:
1. Find all the bugs
2. Fix them
3. Add a comment explaining what each bug was
"""

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def find_maximum(items):
    max_val = 0
    for item in items:
        if item > max_val:
            max_val = item
    return max_val

def reverse_string(text):
    reversed = ""
    for i in range(len(text)):
        reversed = text[i] + reversed
    return reverse

if __name__ == "__main__":
    # Test the functions
    print(calculate_average([]))  # This will crash
    print(find_maximum([-5, -10, -1]))  # Wrong answer
    print(reverse_string("Codex"))  # NameError