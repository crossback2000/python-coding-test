# 실행: python 19.py < input.txt
"""
문제
가장 넓은 영역의 크기
- N×M 격자에서 1은 색칠된 칸, 0은 빈 칸을 의미한다. 상하좌우로 인접한 색칠된 칸이 연결되어 하나의 영역을 이룬다. 가장 넓은 영역의 칸 수를 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000)과 M(1 ≤ M ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 격자 정보가 주어진다.

출력
가장 큰 영역의 칸 수를 출력한다. 색칠된 칸이 없다면 0을 출력한다.

제한
1 ≤ N ≤ 1,000 / 1 ≤ M ≤ 1,000

예제
입력
3 3
110
010
011

출력
4

해설
DFS로 각 영역의 크기를 계산하면서 최대값을 갱신하면 된다.

"""

from typing import Iterable, List


def max_region_area(grid: Iterable[Iterable[int]]) -> int:
    """DFS로 가장 큰 영역 크기를 구한다."""
    board: List[List[int]] = [list(row) for row in grid]
    if not board:
        return 0

    n_rows = len(board)
    n_cols = len(board[0])

    def dfs(r: int, c: int) -> int:
        if not (0 <= r < n_rows and 0 <= c < n_cols):
            return 0
        if board[r][c] == 0:
            return 0

        board[r][c] = 0

        # 현재 칸을 포함해 상하좌우로 확장한 영역의 크기를 더한다.
        size = 1
        size += dfs(r + 1, c)
        size += dfs(r - 1, c)
        size += dfs(r, c + 1)
        size += dfs(r, c - 1)
        return size

    max_size = 0

    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col] == 1:
                area = dfs(row, col)
                max_size = max(max_size, area)

    return max_size


DETAILED_EXPLANATION = """
영역의 크기를 구하는 방법은 연결 요소의 개수를 세는 방식과 거의 동일하다. 색칠된 칸을 발견하면 DFS로 연결된 모든 칸을 방문하면서 카운트를 누적한다. 탐색이 끝났을 때 얻은 크기와 현재까지의 최대 크기를 비교하여 갱신하면 된다. 문제를 해결하기 위해서는 DFS가 연결된 공간을 한 번에 탐색한다는 사실을 이해하고, 방문 처리를 통해 중복 탐색을 피하는 전략을 떠올리면 된다.
"""



def solve() -> None:
    """격자 정보를 입력받아 가장 큰 영역의 크기를 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, m = map(int, first_line.split())
    grid = []
    for _ in range(n):
        line = input().strip()
        while line == "":
            line = input().strip()
        if " " in line:
            row = [int(x) for x in line.split()]
        else:
            row = [int(ch) for ch in line]
        grid.append(row)

    print(max_region_area(grid))


if __name__ == "__main__":
    solve()
