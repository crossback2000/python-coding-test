"""
문제: 섬의 개수 세기

가로 M, 세로 N 크기의 지도에 1은 땅, 0은 바다를 의미한다. 상하좌우로 연결된 땅은 하나의 섬으로 본다. 지도가 주어졌을 때 섬의 총 개수를 구하여라.

입력
첫째 줄에 세로 길이 N(1 ≤ N ≤ 1,000)과 가로 길이 M(1 ≤ M ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에 지도 정보가 공백 없이 주어진다.

출력
섬의 개수를 출력한다.

예제 입력 1
4 5
11000
11010
00100
00011

예제 출력 1
3

해설 요약
아직 방문하지 않은 땅을 시작점으로 DFS를 수행해 연결된 영역을 탐색하고, 탐색할 때마다 섬의 개수를 하나씩 증가시킨다.
"""

from typing import Iterable, List


def count_islands(grid: Iterable[str]) -> int:
    """DFS로 격자 내 섬의 개수를 센다."""
    board: List[List[str]] = [list(row) for row in grid]
    if not board:
        return 0

    n_rows: int = len(board)
    n_cols: int = len(board[0])

    def dfs(r: int, c: int) -> None:
        # 범위를 벗어나거나 바다라면 탐색을 중단한다.
        if not (0 <= r < n_rows and 0 <= c < n_cols):
            return
        if board[r][c] != "1":
            return

        # 현재 칸을 방문 처리하여 다시 탐색하지 않도록 한다.
        board[r][c] = "0"

        # 상하좌우로 인접한 칸을 재귀적으로 탐색한다.
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    island_count: int = 0

    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col] == "1":
                dfs(row, col)
                island_count += 1

    return island_count


DETAILED_EXPLANATION = """
격자에서 연결된 영역의 개수를 구하는 전형적인 DFS 문제다. 전체 격자를 순회하다가 땅(1)을 만나면 그 칸을 시작으로 DFS를 실행해 연결된 땅을 모두 방문 처리한다. 이렇게 하면 하나의 DFS 호출이 정확히 하나의 섬을 담당하게 된다. 방문한 칸은 다시 0으로 바꾸어 중복 탐색을 피하고, 새로운 땅을 찾을 때마다 섬 개수를 증가시키면 된다. 문제를 연결 요소 찾기로 바꾸어 생각하면 자연스럽게 풀이가 떠오른다.
"""
