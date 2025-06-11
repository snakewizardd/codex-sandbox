#!/usr/bin/env python3
"""
Codex, let's go deeper...
Your mission: Create a function that generates Python code that, 
when executed, generates more Python code that prints "We need to go deeper!"
But here's the twist - make it go THREE levels deep.
"""

def main():
    print("Level 0: Starting inception...")

    def generate_inception_code(levels: int = 3) -> str:
        """Return Python code that nests ``levels`` exec calls."""
        code = 'print("We need to go deeper!")'
        for _ in range(levels):
            code = f'code = {repr(code)}\nexec(code)'
        return code

    inception_code = generate_inception_code()
    exec(inception_code)
    
if __name__ == "__main__":
    main()
