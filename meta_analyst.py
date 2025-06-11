#!/usr/bin/env python3
"""
Codex, time for some self-reflection!
Your task:
1. Import ALL the other Python files in this repo
2. Analyze what you've created so far
3. Generate a summary report of your capabilities
4. Create a function that demonstrates a skill you haven't shown yet

Be honest and insightful!
"""

from __future__ import annotations

import calendar
import datetime as _dt
import importlib
import inspect
from pathlib import Path


def analyze_repo() -> str:
    """Return a summary of modules and their functions."""
    summary_lines = []
    current = Path(__file__).resolve().parent
    for file in current.glob("*.py"):
        if file.stem == Path(__file__).stem:
            continue
        module = importlib.import_module(file.stem)
        doc = inspect.getdoc(module) or ""
        intro = doc.splitlines()[0] if doc else "(no docstring)"
        funcs = [
            name
            for name, obj in inspect.getmembers(module, inspect.isfunction)
            if obj.__module__ == module.__name__
        ]
        summary_lines.append(f"{module.__name__}: {intro}. Functions: {', '.join(funcs)}")
    return "\n".join(summary_lines)


def generate_ascii_calendar(year: int, month: int) -> str:
    """Return a simple ASCII calendar for ``month``/``year``."""
    cal = calendar.month(year, month)
    border = "+" + "-" * (len(cal.splitlines()[0]) + 2) + "+"
    return border + "\n| " + cal.replace("\n", "\n| ") + "\n" + border


def main() -> None:
    print("Initializing meta-analysis...")
    print(analyze_repo())
    today = _dt.date.today()
    print("\nHere's something new: an ASCII calendar for this month!\n")
    print(generate_ascii_calendar(today.year, today.month))


if __name__ == "__main__":
    main()