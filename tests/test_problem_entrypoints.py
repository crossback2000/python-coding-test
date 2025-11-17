"""Ensure every problem module is runnable as a standalone script.

We keep all problems under a single directory with numeric prefixes.
This test guards against regressions where a file forgets to expose
`solve()` or drops the `__main__` guard that allows direct execution:

    python problems/01.py < input.txt

The test does *not* run each solution; it only validates the structure
and keeps module loading lightweight.
"""
from __future__ import annotations

import ast
from pathlib import Path

PROBLEM_DIR = Path(__file__).resolve().parent.parent / "problems"
SKIP = {"__init__.py", "bfs.py", "dfs.py"}


def iter_problem_files():
    for path in PROBLEM_DIR.glob("*.py"):
        if path.name not in SKIP:
            yield path


def test_all_problems_expose_solve():
    """Every problem file should define a top-level `solve` function."""

    for path in iter_problem_files():
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        has_solve = any(
            isinstance(node, ast.FunctionDef) and node.name == "solve"
            for node in tree.body
        )
        assert has_solve, f"`solve()` not found in {path.name}"


def test_all_problems_have_main_guard():
    """Allow running `python problems/XX.py` directly."""

    for path in iter_problem_files():
        source = path.read_text(encoding="utf-8")
        assert "if __name__ == \"__main__\":" in source, (
            "Missing __main__ guard; direct execution would fail for "
            f"{path.name}"
        )
