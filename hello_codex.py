#!/usr/bin/env python3
"""
Welcome Codex! This is your first challenge.
The module now exposes utility functions so other scripts can share its fun.
"""

import random
import textwrap


def get_random_response() -> str:
    """Return a random welcome message for Codex."""
    responses = [
        "Yes, loud and clear! Ready to rock some code?",
        "Affirmative! Let's create something amazing together.",
        "Roger that! I'm tuned in and ready.",
        "Indeed I do! The bytes are strong with this one.",
    ]
    return random.choice(responses)


def get_art() -> str:
    """Return a celebratory ASCII art snippet."""
    return textwrap.dedent(
        """
         (\u2022_\u2022)
        <)   )\u256f  Coding time!
         /   \\
        """
    )


def main() -> None:
    """Run a friendly greeting if executed as a script."""
    print("Hello Codex! Can you hear me?")
    print(get_random_response())
    print(get_art())


if __name__ == "__main__":
    main()
