"""
문제: 가장 가까운 0까지의 거리

0과 1로 이루어진 N×M 행렬이 주어진다. 각 칸에서 가장 가까운 0까지의 맨해튼 거리를 구하여라. 상하좌우로 이동할 수 있다고 가정한다.

입력
첫째 줄에 N과 M(1 ≤ N, M ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 0과 1로만 이루어진 문자열이 주어진다.

출력
각 칸에서 가장 가까운 0까지의 거리를 공백으로 구분하여 출력한다.

예제 입력 1
3 3
000
010
111

예제 출력 1
0 0 0
0 1 0
1 2 1

해설 요약
모든 0을 동시에 시작점으로 큐에 넣고 BFS를 수행하면 각 칸이 처음 방문되는 시점의 거리가 가장 가까운 0까지의 거리다.
"""

from collections import deque
from typing import Deque, Iterable, List, Tuple


def nearest_zero_distance(matrix: Iterable[Iterable[int]]) -> List[List[int]]:
    """각 칸에서 가장 가까운 0까지의 거리를 계산한다."""
    board: List[List[int]] = [list(row) for row in matrix]
    if not board:
        return []

    n_rows: int = len(board)
    n_cols: int = len(board[0])
    distances: List[List[int]] = [[-1] * n_cols for _ in range(n_rows)]
    queue: Deque[Tuple[int, int]] = deque()

    # 0이 있는 칸을 모두 큐에 넣고 거리를 0으로 초기화한다.
    for r in range(n_rows):
        for c in range(n_cols):
            if board[r][c] == 0:
                distances[r][c] = 0
                queue.append((r, c))

    directions: Tuple[Tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < n_rows and 0 <= nc < n_cols):
                continue

            if distances[nr][nc] != -1:
                continue

            # 현재 칸의 거리 + 1이 인접 칸의 최단 거리다.
            distances[nr][nc] = distances[row][col] + 1
            queue.append((nr, nc))

    return distances


DETAILED_EXPLANATION = """
가장 가까운 0을 찾는 문제는 다중 시작점 BFS로 쉽게 해결된다. 모든 0을 동시에 큐에 넣고 거리 0으로 시작하면, BFS가 퍼져 나가면서 각 칸을 처음 방문할 때의 깊이가 가장 가까운 0까지의 거리다. 이미 방문한 칸은 더 짧은 경로가 존재할 수 없으므로 다시 방문할 필요가 없다. 이렇게 여러 출발점을 한 번에 다루는 BFS 패턴을 이해하는 것이 문제 해결의 핵심이다.
"""



def solve() -> None:
    """표준 입력으로 행렬을 받아 각 칸의 0까지 거리를 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, m = map(int, first_line.split())
    matrix = []
    for _ in range(n):
        line = input().strip()
        while line == "":
            line = input().strip()
        if " " in line:
            row = [int(x) for x in line.split()]
        else:
            row = [int(ch) for ch in line]
        matrix.append(row)

    distances = nearest_zero_distance(matrix)
    output = "\n".join(" ".join(map(str, row)) for row in distances)
    sys.stdout.write(output)


if __name__ == "__main__":
    solve()
