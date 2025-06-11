#!/usr/bin/env python3
"""
CODEX: THE MIND BENDER

Create a program that generates a visual quine - code that:
1. When run, displays its own source code as ASCII art
2. The ASCII art version is also valid Python that does something different
3. That second program generates a third valid program
4. Each level reveals a hidden message

Example flow:
Level 1: Run mind_bender.py → See ASCII art of the source
Level 2: Copy/run the ASCII art → It's valid Python that creates a fractal
Level 3: The fractal contains hidden code that's also valid Python

Make each level do something surprising and beautiful.
"""

def main():
    print("Reality has layers...")
    # TODO: Create the inception of visual code
    
if __name__ == "__main__":
    main()