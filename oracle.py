# !/usr/bin/env python3
"""The Oracle: analyze Codex outputs and generate challenges."""
from __future__ import annotations

import ast
import json
from pathlib import Path


def analyze_python_files() -> dict:
    """Analyze Python files and return summary metrics."""
    metrics = {
        "files": 0,
        "functions": 0,
        "docstrings": 0,
        "try_statements": 0,
        "async_functions": 0,
    }
    for path in Path('.').glob('*.py'):
        if path.name == Path(__file__).name:
            continue
        metrics["files"] += 1
        source = path.read_text()
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                metrics["functions"] += 1
                if ast.get_docstring(node):
                    metrics["docstrings"] += 1
                if node.returns is not None and isinstance(node, ast.AsyncFunctionDef):
                    metrics["async_functions"] += 1
            elif isinstance(node, ast.Try):
                metrics["try_statements"] += 1
            elif isinstance(node, ast.AsyncFunctionDef):
                metrics["functions"] += 1
                metrics["async_functions"] += 1
                if ast.get_docstring(node):
                    metrics["docstrings"] += 1
    return metrics


def generate_report(metrics: dict) -> str:
    """Generate a textual report from metrics."""
    lines = ["THE ORACLE REPORT", "==================", ""]
    lines.append(f"Python files analyzed: {metrics['files']}")
    lines.append(f"Total functions: {metrics['functions']}")
    lines.append(f"Functions with docstrings: {metrics['docstrings']}")
    lines.append(f"Try/except blocks: {metrics['try_statements']}")
    lines.append(f"Async functions: {metrics['async_functions']}")
    # identify weaknesses
    weaknesses = []
    if metrics['async_functions'] == 0:
        weaknesses.append('lack of asynchronous programming')
    if metrics['try_statements'] == 0:
        weaknesses.append('minimal error handling')
    if metrics['docstrings'] < metrics['functions']:
        weaknesses.append('incomplete documentation')
    lines.append("")
    lines.append("Identified weaknesses: " + ", ".join(weaknesses))
    return "\n".join(lines), weaknesses


def generate_challenges(weaknesses: list[str]) -> list[dict]:
    """Generate challenges exploiting weaknesses."""
    challenges = []
    if 'lack of asynchronous programming' in weaknesses:
        challenges.append({
            'title': 'Async Network Fetcher',
            'description': 'Write an async Python program that fetches multiple URLs concurrently and saves their content.'
        })
    if 'minimal error handling' in weaknesses:
        challenges.append({
            'title': 'Robust Calculator',
            'description': 'Create a calculator that gracefully handles division by zero and invalid input.'
        })
    if 'incomplete documentation' in weaknesses:
        challenges.append({
            'title': 'Document Everything',
            'description': 'Add comprehensive docstrings and examples to all existing modules.'
        })
    return challenges


def generate_solutions(challenges: list[dict]) -> dict:
    """Generate naive solution snippets for each challenge."""
    solutions: dict[str, str] = {}
    for ch in challenges:
        if ch['title'] == 'Async Network Fetcher':
            solutions[ch['title']] = (
                'import asyncio, aiohttp\n\n'
                'async def fetch(url, session):\n'
                '    async with session.get(url) as resp:\n'
                '        return await resp.text()\n\n'
                'async def main(urls):\n'
                '    async with aiohttp.ClientSession() as s:\n'
                '        texts = await asyncio.gather(*(fetch(u, s) for u in urls))\n'
                '    for text in texts: print(len(text))\n\n'
                'if __name__ == "__main__":\n'
                '    import sys\n'
                '    asyncio.run(main(sys.argv[1:]))\n'
            )
        elif ch['title'] == 'Robust Calculator':
            solutions[ch['title']] = (
                'def divide(a, b):\n'
                '    try:\n'
                '        return a / b\n'
                '    except ZeroDivisionError:\n'
                '        return float("inf")\n\n'
                'def parse_number(text):\n'
                '    try:\n'
                '        return float(text)\n'
                '    except ValueError:\n'
                '        raise ValueError("Invalid number")\n'
            )
        elif ch['title'] == 'Document Everything':
            solutions[ch['title']] = '# Add docstrings to all modules per PEP 257.'
    return solutions


def main() -> None:
    metrics = analyze_python_files()
    report, weaknesses = generate_report(metrics)
    print(report)
    challenges = generate_challenges(weaknesses)
    print("\nGenerated Challenges:")
    print(json.dumps(challenges, indent=2))
    solutions = generate_solutions(challenges)
    print("\nSolutions:")
    print(json.dumps(solutions, indent=2))


if __name__ == "__main__":
    main()
