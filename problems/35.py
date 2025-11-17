# 실행: python 35.py < input.txt
"""
문제: 로봇의 체크포인트 수거 (BFS + 비트마스크 DP)

격자 위에 로봇이 있으며, 특정 칸에 체크포인트가 있다. 로봇은 상하좌우로 이동할 수 있고
벽을 통과할 수 없다. 모든 체크포인트를 방문하는 데 필요한 최소 이동 횟수를 구하라.

입력
첫째 줄에 격자의 크기 R, C(1 ≤ R, C ≤ 15)가 주어진다.
이후 R개의 줄에 격자를 나타내는 문자열이 주어진다. 문자 의미는 다음과 같다.
- 'S': 로봇의 시작 위치 (하나만 존재)
- 'X': 체크포인트
- '#': 벽
- '.': 빈 칸
모든 체크포인트를 방문할 수 있는 입력만 주어진다. 체크포인트의 수는 최대 10개다.

출력
모든 체크포인트를 방문하기 위한 최소 이동 횟수를 출력한다.

예제 입력 1
3 4
S.X.
.#..
..X.

예제 출력 1
5

해설 요약
모든 체크포인트 사이의 최단 거리를 BFS로 미리 구해 그래프 형태로 변환한다.
이후 "모든 노드를 한 번씩 방문" 문제는 비트마스크 DP로 해결할 수 있다.
상태 dp[mask][i]는 현재 i번째 체크포인트에 있고 mask에 방문 기록이 있을 때의 최소 거리다.
"""

from collections import deque
from typing import Dict, List, Tuple

Grid = List[str]
Point = Tuple[int, int]


def bfs_shortest(grid: Grid, start: Point) -> Dict[Point, int]:
    """주어진 시작점에서 모든 도달 가능한 칸까지의 최단 거리를 구한다."""

    rows, cols = len(grid), len(grid[0])
    queue: deque[Point] = deque([start])
    distance = {start: 0}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # 격자 범위 내이고 벽이 아니며 아직 방문하지 않았다면 이동한다.
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in distance:
                distance[(nr, nc)] = distance[(r, c)] + 1
                queue.append((nr, nc))
    return distance


def shortest_path_collect_all(grid: Grid) -> int:
    """모든 체크포인트를 방문하는 최단 거리를 구한다."""

    rows, cols = len(grid), len(grid[0])

    # 시작점과 체크포인트를 찾는다.
    checkpoints: List[Point] = []
    start: Point = (-1, -1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "X":
                checkpoints.append((r, c))

    # 시작점을 checkpoints 리스트의 맨 앞에 넣어 인덱스를 맞춘다.
    all_points = [start] + checkpoints
    k = len(all_points)

    # 모든 포인트 쌍 사이 최단 거리를 BFS로 구한다.
    dist_matrix = [[-1] * k for _ in range(k)]
    for i, point in enumerate(all_points):
        distances = bfs_shortest(grid, point)
        for j, other in enumerate(all_points):
            dist_matrix[i][j] = distances.get(other, -1)

    # 비연결인 경우는 주어지지 않는다고 했지만, 방어적으로 체크한다.
    for i in range(k):
        for j in range(k):
            if dist_matrix[i][j] == -1:
                raise ValueError("체크포인트가 서로 도달 불가합니다")

    # 비트마스크 DP: dp[mask][i]는 mask 상태에서 i 위치에 있을 때의 최소 거리
    total_mask = 1 << k
    INF = 10 ** 12
    dp = [[INF] * k for _ in range(total_mask)]

    # 시작점은 index 0, 방문 비트마스크도 1 << 0 으로 초기화
    dp[1][0] = 0

    for mask in range(total_mask):
        for i in range(k):
            if dp[mask][i] == INF:
                continue
            # i에서 다른 포인트 j로 이동하여 방문하지 않은 비트를 추가한다.
            for j in range(1, k):  # 체크포인트만 순회 (0은 시작점)
                next_bit = 1 << j
                if mask & next_bit:
                    continue  # 이미 방문
                next_mask = mask | next_bit
                candidate = dp[mask][i] + dist_matrix[i][j]
                if candidate < dp[next_mask][j]:
                    dp[next_mask][j] = candidate

    # 모든 체크포인트를 방문한 상태(mask == (1<<k)-1)에서의 최소 값을 찾는다.
    full_mask = total_mask - 1
    return min(dp[full_mask])


DETAILED_EXPLANATION = """
모든 좌표에서 BFS를 하면 각 포인트 사이의 최단 거리를 얻는다. 시작점과 체크포인트를 합쳐 k개라면 거리 행렬
구성 비용은 O(k * R * C)이다. 이후 "모든 체크포인트 방문" 문제는 외판원 순회(TSP)와 동일하며, 상태 공간이
2^k * k 로 충분히 작다(k ≤ 11). dp[mask][i]에서 방문하지 않은 j로 이동하며 최솟값을 갱신하면 된다. 최종적으로
모든 비트가 켜진 상태의 최소 거리를 답으로 선택한다.
"""


def solve() -> None:
    """격자를 입력받아 로봇이 모든 체크포인트를 방문하는 최소 이동 거리를 출력한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    r, c = map(int, line.split())
    grid = [list(input().strip()) for _ in range(r)]
    grid_str = ["".join(row) for row in grid]
    print(shortest_path_collect_all(grid_str))


if __name__ == "__main__":
    solve()
