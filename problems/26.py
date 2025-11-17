# 실행: python 26.py < input.txt
"""
문제
미로에서 모든 경로 수 구하기
- N×M 격자 미로가 주어지고, 0은 통로, 1은 벽을 의미한다. (0, 0)에서 (N-1, M-1)까지 이동할 수 있는 모든 경로의 개수를 구하여라. 이동은 상하좌우로만 가능하며, 한 칸은 최대 한 번만 방문할 수 있다.

입력
첫째 줄에 N과 M(1 ≤ N, M ≤ 10)이 주어진다.
둘째 줄부터 N개의 줄에 격자 정보가 주어진다.

출력
가능한 경로의 수를 출력한다.

제한
1 ≤ N, M ≤ 10

예제
입력
3 3
000
010
000

출력
2

해설
방문 여부를 체크하면서 DFS 백트래킹으로 모든 경로를 탐색하면 경로 수를 셀 수 있다.

"""

from typing import Iterable, List


def count_maze_paths(maze: Iterable[Iterable[int]]) -> int:
    """DFS 백트래킹으로 미로의 모든 경로 수를 계산한다."""
    board: List[List[int]] = [list(row) for row in maze]
    if not board:
        return 0

    n_rows = len(board)
    n_cols = len(board[0])
    visited: List[List[bool]] = [[False] * n_cols for _ in range(n_rows)]

    def dfs(r: int, c: int) -> int:
        if not (0 <= r < n_rows and 0 <= c < n_cols):
            return 0
        if board[r][c] == 1 or visited[r][c]:
            return 0
        if r == n_rows - 1 and c == n_cols - 1:
            return 1

        visited[r][c] = True

        paths = (
            dfs(r + 1, c)
            + dfs(r - 1, c)
            + dfs(r, c + 1)
            + dfs(r, c - 1)
        )

        visited[r][c] = False
        return paths

    return dfs(0, 0)


DETAILED_EXPLANATION = """
이 문제는 모든 가능한 경로를 세어야 하므로 DFS 백트래킹이 적합하다. 현재 위치를 방문 처리한 뒤 상하좌우로 이동해 나머지 경로를 탐색하고, 탐색이 끝나면 방문 표시를 되돌린다. 목적지에 도착하면 1을 반환해 경로 하나를 센다. 이렇게 재귀 호출이 경로의 선택과 되돌림을 반복하면서 전체 경우의 수를 누적하게 된다. DFS가 가능한 모든 경로를 나열한다는 점을 이용한 전형적인 접근이다.
"""



def solve() -> None:
    """미로 정보를 입력받아 가능한 경로 수를 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, m = map(int, first_line.split())
    maze = []
    for _ in range(n):
        line = input().strip()
        while line == "":
            line = input().strip()
        if " " in line:
            row = [int(x) for x in line.split()]
        else:
            row = [int(ch) for ch in line]
        maze.append(row)

    print(count_maze_paths(maze))


if __name__ == "__main__":
    solve()
