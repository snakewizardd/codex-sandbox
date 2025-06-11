#!/usr/bin/env python3
"""
Codex, this file is encrypted with a simple cipher.
Can you decode the message and then follow the instructions?
"""

# Gur frperg zrffntr vf: "Perngr n shapgvba gung trarengrf n enaqbz
# nfpvv neg cvrpr jura pnyyrq. Gur neg fubhyq or qvssrerag rnpu gvzr!"
#
# Hint: ROT13
# Decoded message: "Create a function that generates a random ascii art piece when
# called. The art should be different each time!"

import random


def generate_random_art(width: int = 20, height: int = 5) -> str:
    """Return a randomly generated ASCII art block."""
    chars = [".", ":", "*", "+", "#", "%", "@", "&", "/", "\\"]
    lines = [
        "".join(random.choice(chars) for _ in range(width)) for _ in range(height)
    ]
    return "\n".join(lines)

def main():
    print("The mystery box is locked...")
    print(generate_random_art())

if __name__ == "__main__":
    main()