from problems.dfs import (
    TreeNode as DFSTreeNode,
    binary_tree_path_sums,
    count_islands,
    count_maze_paths,
    count_target_sum,
    enumerate_all_paths,
    exist_word,
    generate_combinations,
    generate_permutations,
    max_region_area,
    restore_ip_addresses,
)
from problems.bfs import (
    TreeNode as BFSTreeNode,
    level_order_values,
    minimum_depth,
    minimum_knight_moves,
    minimum_turns_to_unlock,
    nearest_zero_distance,
    shortest_path_in_maze,
    shortest_steps_from_start,
    spread_time,
    time_to_rot_all,
    word_ladder_length,
)


def test_count_islands() -> None:
    grid = [
        "11000",
        "11010",
        "00100",
        "00011",
    ]
    assert count_islands(grid) == 4


def test_max_region_area() -> None:
    grid = [
        [1, 1, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    assert max_region_area(grid) == 6


def test_exist_word() -> None:
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exist_word(board, "ABCCED") is True
    assert exist_word(board, "SEE") is True
    assert exist_word(board, "ABCB") is False


def test_generate_permutations() -> None:
    perms = generate_permutations([1, 2, 3])
    assert sorted(perms) == sorted(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )


def test_generate_combinations() -> None:
    combos = generate_combinations([1, 2, 3, 4], 2)
    assert sorted(combos) == sorted(
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    )


def test_count_target_sum() -> None:
    assert count_target_sum([1, 1, 1, 1, 1], 3) == 5


def test_count_maze_paths() -> None:
    maze = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert count_maze_paths(maze) == 2


def test_enumerate_all_paths() -> None:
    graph = [[1, 2], [3], [3], []]
    paths = enumerate_all_paths(graph)
    assert sorted(paths) == sorted([[0, 1, 3], [0, 2, 3]])


def test_binary_tree_path_sums() -> None:
    root = DFSTreeNode(5)
    root.left = DFSTreeNode(4, DFSTreeNode(11, DFSTreeNode(7), DFSTreeNode(2)))
    root.right = DFSTreeNode(8, DFSTreeNode(13), DFSTreeNode(4, None, DFSTreeNode(1)))
    assert sorted(binary_tree_path_sums(root)) == sorted([27, 22, 26, 18])


def test_restore_ip_addresses() -> None:
    result = restore_ip_addresses("25525511135")
    assert sorted(result) == sorted(["255.255.11.135", "255.255.111.35"])


def test_shortest_path_in_maze() -> None:
    maze = [
        "101111",
        "101010",
        "101011",
        "111011",
    ]
    assert shortest_path_in_maze(maze) == 15


def test_minimum_knight_moves() -> None:
    assert minimum_knight_moves(8, (0, 0), (7, 7)) == 6


def test_minimum_depth() -> None:
    root = BFSTreeNode(1)
    root.left = BFSTreeNode(2)
    root.right = BFSTreeNode(3, BFSTreeNode(4), BFSTreeNode(5))
    assert minimum_depth(root) == 2


def test_time_to_rot_all() -> None:
    grid = [
        [1, 0, -1, 0, 0, 0],
        [0, 0, 1, 0, -1, 0],
        [0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, -1, 1],
    ]
    assert time_to_rot_all(grid) == 4


def test_word_ladder_length() -> None:
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert word_ladder_length("hit", "cog", words) == 5


def test_level_order_values() -> None:
    root = BFSTreeNode(3)
    root.left = BFSTreeNode(9)
    root.right = BFSTreeNode(20, BFSTreeNode(15), BFSTreeNode(7))
    assert level_order_values(root) == [[3], [9, 20], [15, 7]]


def test_shortest_steps_from_start() -> None:
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    assert shortest_steps_from_start(graph, 0) == {0: 0, 1: 1, 2: 1, 3: 2}


def test_nearest_zero_distance() -> None:
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    assert nearest_zero_distance(matrix) == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
    ]


def test_spread_time() -> None:
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    assert spread_time(graph, 0) == 2


def test_spread_time_unreachable() -> None:
    graph = {0: [1], 1: [0], 2: []}
    assert spread_time(graph, 0) == -1


def test_minimum_turns_to_unlock() -> None:
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    assert minimum_turns_to_unlock(deadends, "0202") == 6


def test_minimum_turns_to_unlock_unreachable() -> None:
    deadends = ["0000"]
    assert minimum_turns_to_unlock(deadends, "8888") == -1
