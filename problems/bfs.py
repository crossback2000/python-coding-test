"""BFS 문제 모듈 로더 (단일 디렉터리 구조).

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


_tree_min_depth = _load_module("11.py")
TreeNode = _tree_min_depth.TreeNode
minimum_depth = _tree_min_depth.minimum_depth

_level_order = _load_module("12.py")
level_order_values = _level_order.level_order_values

_graph_shortest_steps = _load_module("16.py")
shortest_steps_from_start = _graph_shortest_steps.shortest_steps_from_start

_matrix_distance = _load_module("21.py")
nearest_zero_distance = _matrix_distance.nearest_zero_distance

_maze_shortest_path = _load_module("23.py")
shortest_path_in_maze = _maze_shortest_path.shortest_path_in_maze

_knight_moves = _load_module("24.py")
minimum_knight_moves = _knight_moves.minimum_knight_moves

_spread_time = _load_module("20.py")
spread_time = _spread_time.spread_time

_rotting_oranges = _load_module("22.py")
time_to_rot_all = _rotting_oranges.time_to_rot_all

_open_lock = _load_module("28.py")
minimum_turns_to_unlock = _open_lock.minimum_turns_to_unlock

_word_ladder = _load_module("30.py")
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
