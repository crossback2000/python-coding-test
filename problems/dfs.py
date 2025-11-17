"""DFS 문제 모듈 로더 (단일 디렉터리 구조).

숫자로 시작하는 파일명을 직접 import 할 수 없으므로 importlib로 로드한다.
"""
from __future__ import annotations

from importlib import util
from pathlib import Path
from types import ModuleType

PACKAGE_DIR = Path(__file__).resolve().parent


def _load_module(filename: str) -> ModuleType:
    module_name = f"{__name__}.{filename.replace('.', '_')}"
    module_path = PACKAGE_DIR / filename
    spec = util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:  # pragma: no cover - import error path
        raise ImportError(f"Failed to load module from {module_path}")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_combinations = _load_module("13.py")
generate_combinations = _combinations.generate_combinations

_permutations = _load_module("14.py")
generate_permutations = _permutations.generate_permutations

_target_sum = _load_module("15.py")
count_target_sum = _target_sum.count_target_sum

_tree_path_sums = _load_module("17.py")
TreeNode = _tree_path_sums.TreeNode
binary_tree_path_sums = _tree_path_sums.binary_tree_path_sums

_island_count = _load_module("18.py")
count_islands = _island_count.count_islands

_max_region = _load_module("19.py")
max_region_area = _max_region.max_region_area

_maze_paths = _load_module("26.py")
count_maze_paths = _maze_paths.count_maze_paths

_all_paths = _load_module("25.py")
enumerate_all_paths = _all_paths.enumerate_all_paths

_word_search = _load_module("27.py")
exist_word = _word_search.exist_word

_restore_ip = _load_module("29.py")
restore_ip_addresses = _restore_ip.restore_ip_addresses

__all__ = [
    "TreeNode",
    "binary_tree_path_sums",
    "count_islands",
    "count_maze_paths",
    "count_target_sum",
    "enumerate_all_paths",
    "exist_word",
    "generate_combinations",
    "generate_permutations",
    "max_region_area",
    "restore_ip_addresses",
]
