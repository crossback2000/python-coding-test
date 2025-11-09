"""너비 우선 탐색 문제 모음.

문제 파일명이 난이도 순서를 나타내도록 숫자로 시작하기 때문에 일반적인
파이썬 모듈 import 구문을 사용할 수 없다. 따라서 이 모듈에서는
``importlib``을 이용해 파일 경로에서 직접 모듈을 로드한 뒤, 외부에 공개할
함수와 클래스를 할당한다.
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


_tree_min_depth = _load_module("01_tree_min_depth.py")
TreeNode = _tree_min_depth.TreeNode
minimum_depth = _tree_min_depth.minimum_depth

_level_order = _load_module("02_level_order.py")
level_order_values = _level_order.level_order_values

_graph_shortest_steps = _load_module("06_graph_shortest_steps.py")
shortest_steps_from_start = _graph_shortest_steps.shortest_steps_from_start

_matrix_distance = _load_module("11_matrix_distance.py")
nearest_zero_distance = _matrix_distance.nearest_zero_distance

_maze_shortest_path = _load_module("13_maze_shortest_path.py")
shortest_path_in_maze = _maze_shortest_path.shortest_path_in_maze

_knight_moves = _load_module("14_knight_moves.py")
minimum_knight_moves = _knight_moves.minimum_knight_moves

_spread_time = _load_module("10_spread_time.py")
spread_time = _spread_time.spread_time

_rotting_oranges = _load_module("12_rotting_oranges.py")
time_to_rot_all = _rotting_oranges.time_to_rot_all

_open_lock = _load_module("18_open_lock.py")
minimum_turns_to_unlock = _open_lock.minimum_turns_to_unlock

_word_ladder = _load_module("20_word_ladder.py")
word_ladder_length = _word_ladder.word_ladder_length

__all__ = [
    "TreeNode",
    "level_order_values",
    "minimum_depth",
    "minimum_knight_moves",
    "minimum_turns_to_unlock",
    "nearest_zero_distance",
    "shortest_path_in_maze",
    "shortest_steps_from_start",
    "spread_time",
    "time_to_rot_all",
    "word_ladder_length",
]
