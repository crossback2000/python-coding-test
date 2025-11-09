"""
문제: 미로 탐색 최단 거리 구하기

N×M 크기의 격자 미로가 주어진다. 격자에는 숫자 0과 1이 적혀 있으며, 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸을 의미한다. (1, 1)에서 출발하여 (N, M)까지 이동할 때 반드시 상하좌우로 인접한 칸으로만 움직일 수 있다. 이동 가능한 입력만 주어졌을 때, 목적지에 도달하기 위해 지나야 하는 칸의 최소 개수를 구하여라. 시작점과 도착점도 이동 칸 수에 포함한다.

입력
첫째 줄에 세로 길이 N(2 ≤ N ≤ 100)과 가로 길이 M(2 ≤ M ≤ 100)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 길이 M의 0과 1로만 이루어진 문자열이 주어진다. 문자열의 j번째 문자는 (i, j) 위치의 칸이 이동 가능한지 여부를 나타낸다.

출력
최소 이동 칸 수를 정수 한 줄로 출력한다.

예제 입력 1
4 6
101111
101010
101011
111011

예제 출력 1
15

예제 입력 2
2 3
111
111

예제 출력 2
4

해설 요약
BFS로 시작점에서부터 거리를 한 칸씩 확장하며 방문하면 가장 먼저 도착하는 순간의 거리가 곧 최단 거리이다.
"""

from collections import deque
from typing import Deque, Iterable, List, Tuple


def shortest_path_in_maze(board: Iterable[str]) -> int:
    """너비 우선 탐색으로 최단 이동 칸 수를 계산한다."""
    # board를 리스트로 바꾸어 인덱스로 접근하기 쉽게 만든다.
    grid: List[str] = list(board)
    if not grid:
        raise ValueError("미로 데이터가 비어 있습니다.")

    n_rows: int = len(grid)
    n_cols: int = len(grid[0])

    # 방문 여부와 함께 최소 이동 칸 수를 기록할 2차원 배열을 만든다.
    distances: List[List[int]] = [[0] * n_cols for _ in range(n_rows)]

    # (행, 열) 좌표를 큐에 넣고, 시작 위치의 거리를 1로 설정한다.
    queue: Deque[Tuple[int, int]] = deque([(0, 0)])
    distances[0][0] = 1

    # 상, 하, 좌, 우 네 방향으로 이동하기 위한 델타 값을 준비한다.
    directions: Tuple[Tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        row, col = queue.popleft()
        current_distance: int = distances[row][col]

        # 목적지에 도달하면 그때의 거리를 반환한다.
        if row == n_rows - 1 and col == n_cols - 1:
            return current_distance

        # 네 방향으로 한 칸씩 이동해 본다.
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc

            # 미로 범위를 벗어나는 경우는 건너뛴다.
            if not (0 <= next_row < n_rows and 0 <= next_col < n_cols):
                continue

            # 벽(0)인 칸은 이동할 수 없다.
            if grid[next_row][next_col] == "0":
                continue

            # 아직 방문하지 않은 칸이라면 거리를 기록하고 큐에 넣는다.
            if distances[next_row][next_col] == 0:
                distances[next_row][next_col] = current_distance + 1
                queue.append((next_row, next_col))

    raise ValueError("도착 지점에 도달할 수 없습니다.")


DETAILED_EXPLANATION = """
문제를 풀 때는 우선 격자를 그래프로 바라본다. 각 칸은 정점이 되고, 상하좌우로 이동 가능한 칸 사이에 간선이 있다고 생각하면 된다. 모든 간선의 가중치가 1이므로 최단 거리를 구할 때는 BFS가 가장 적합하다. 시작 위치에서부터 큐에 넣어 한 칸씩 넓혀 가며 이동하면, 어떤 칸을 처음 방문할 때 이미 최단 경로가 결정된다. 특히 목적지를 최초로 꺼내는 순간의 거리는 항상 최단 거리이므로 그 값을 곧바로 반환하면 된다. 이렇게 그래프 관점으로 사고하면 왜 BFS가 답이 되는지 자연스럽게 이해할 수 있다.
"""



def solve() -> None:
    """미로 입력을 받아 최단 이동 칸 수를 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, m = map(int, first_line.split())
    board = []
    for _ in range(n):
        line = input().strip()
        while line == "":
            line = input().strip()
        board.append(line)

    print(shortest_path_in_maze(board))


if __name__ == "__main__":
    solve()
