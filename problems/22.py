# 실행: python 22.py < input.txt
"""
문제: 토마토가 모두 익는 최소 시간

N×M 격자 상자에 토마토가 보관되어 있다. 값이 1이면 익은 토마토, 0이면 익지 않은 토마토, -1이면 빈 칸을 의미한다. 하루가 지나면 익은 토마토와 인접한 네 방향의 익지 않은 토마토가 익는다. 모든 토마토가 익을 때까지 최소 며칠이 걸리는지 계산하라. 만약 모두 익힐 수 없다면 -1을 출력한다.

입력
첫째 줄에 M(1 ≤ M ≤ 1,000), N(1 ≤ N ≤ 1,000)이 주어진다.
이후 N개의 줄에 걸쳐 각 줄마다 M개의 정수가 공백 없이 주어진다.

출력
모든 토마토가 익는 데 걸리는 최소 일수를 출력하고, 불가능하다면 -1을 출력한다.

예제 입력 1
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1

예제 출력 1
4

해설 요약
여러 시작점에서 동시에 확산하는 상황이므로 모든 익은 토마토를 초기 큐에 넣고 BFS를 돌리면 가장 마지막으로 익는 토마토까지의 일수가 정답이다.
"""

from collections import deque
from typing import Deque, Iterable, List, Tuple


def time_to_rot_all(grid: Iterable[Iterable[int]]) -> int:
    """모든 토마토가 익는 최소 일수를 계산한다."""
    board: List[List[int]] = [list(row) for row in grid]
    if not board:
        return 0

    n_rows: int = len(board)
    n_cols: int = len(board[0])

    queue: Deque[Tuple[int, int]] = deque()
    unripe_count: int = 0

    # 초기 상태에서 익은 토마토를 모두 큐에 넣는다.
    for r in range(n_rows):
        for c in range(n_cols):
            if board[r][c] == 1:
                queue.append((r, c))
            elif board[r][c] == 0:
                unripe_count += 1

    # 익지 않은 토마토가 없다면 0일이 걸린다.
    if unripe_count == 0:
        return 0

    days: int = 0
    directions: Tuple[Tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        # 하루 단위로 묶어서 처리하기 위해 현재 큐 크기만큼 반복한다.
        for _ in range(len(queue)):
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < n_rows and 0 <= nc < n_cols):
                    continue

                if board[nr][nc] != 0:
                    continue

                # 인접한 익지 않은 토마토가 익는다.
                board[nr][nc] = 1
                unripe_count -= 1
                queue.append((nr, nc))

        days += 1

    # 모든 토마토가 익었다면 마지막으로 증가한 days - 1이 정답이다.
    return days - 1 if unripe_count == 0 else -1


DETAILED_EXPLANATION = """
동시에 여러 지점에서 확산하는 문제는 다중 시작점 BFS로 접근한다. 모든 익은 토마토를 큐에 넣고 하루 단위로 확산을 반복하면, 큐에 남아 있는 칸들은 같은 날짜에 익게 된다. 한 레벨의 탐색이 끝날 때마다 하루를 증가시키고, 새로운 칸이 익을 때마다 미방문 토마토 수를 감소시킨다. 탐색 종료 후 미방문 토마토가 없으면 걸린 날짜가 답이고, 남아 있다면 전부 익히지 못한 것이므로 -1을 출력한다. 이러한 사고 과정을 통해 다중 시작점을 처리하는 BFS 패턴을 익힐 수 있다.
"""



def solve() -> None:
    """토마토 상자 상태를 입력받아 모두 익는 시간을 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    m, n = map(int, first_line.split())
    grid = []
    for _ in range(n):
        line = input().strip()
        while line == "":
            line = input().strip()
        parts = line.split()
        if len(parts) == m:
            row = [int(x) for x in parts]
        else:
            row = [int(ch) for ch in line]
        grid.append(row)

    print(time_to_rot_all(grid))


if __name__ == "__main__":
    solve()
