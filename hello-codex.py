#!/usr/bin/env python3
"""
Welcome Codex! This is your first challenge.
TODO: Make this script greet you back in a creative way
"""

import random
import textwrap


def main():
    print("Hello Codex! Can you hear me?")
    # A surprise response from Codex
    responses = [
        "Yes, loud and clear! Ready to rock some code?",
        "Affirmative! Let's create something amazing together.",
        "Roger that! I'm tuned in and ready.",
        "Indeed I do! The bytes are strong with this one.",
    ]
    art = textwrap.dedent(
        """
         (\u2022_\u2022)
        <)   )\u256f  Coding time!
         /   \\
        """
    )
    print(random.choice(responses))
    print(art)


if __name__ == "__main__":
    main()

