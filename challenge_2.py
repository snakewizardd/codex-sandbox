#!/usr/bin/env python3
"""
Codex, you did great with the first challenge!
Now let's see if you can make these two scripts talk to each other.
This script will borrow a greeting from ``hello_codex.py`` and display it.
"""

from hello_codex import get_random_response, get_art

def main():
    print("I'm challenge_2.py and I'm feeling lonely...")
    # Receive a friendly response from hello_codex
    print(get_random_response())
    print(get_art())
    
if __name__ == "__main__":
    main()

