"""
문제: 체스 나이트의 최소 이동 횟수

체스판 위에서 나이트 말은 (2, 1) 형태로 이동할 수 있다. L자 모양의 이동을 반복하여 시작 칸에서 목표 칸으로 이동할 때 필요한 최소 이동 횟수를 구하여라.

입력
첫째 줄에 체스판의 한 변 길이 N(1 ≤ N ≤ 500)이 주어진다.
둘째 줄에 시작 위치 r1, c1이 주어지고, 셋째 줄에 도착 위치 r2, c2가 주어진다. 좌표는 0부터 시작하며, 항상 체스판 내부에 있다.

출력
나이트가 (r1, c1)에서 (r2, c2)로 이동하는 데 필요한 최소 이동 횟수를 출력한다.

예제 입력 1
8
0 0
7 7

예제 출력 1
6

예제 입력 2
4
0 0
1 2

예제 출력 2
1

해설 요약
나이트의 모든 이동 간선의 가중치는 동일하므로, 시작 위치에서 BFS를 실행하면 가장 먼저 도착 위치를 꺼냈을 때의 깊이가 정답이다.
"""

from collections import deque
from typing import Deque, List, Tuple


def minimum_knight_moves(n: int, start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    """나이트가 목표 칸으로 이동하는 최소 횟수를 반환한다."""
    # 시작과 목표가 같다면 이동할 필요가 없다.
    if start == goal:
        return 0

    # 모든 칸을 아직 방문하지 않았음을 표시하기 위해 -1로 초기화한다.
    visited: List[List[int]] = [[-1] * n for _ in range(n)]
    sr, sc = start
    visited[sr][sc] = 0

    queue: Deque[Tuple[int, int]] = deque([start])

    # 나이트가 이동할 수 있는 8가지 방향을 미리 나열해 둔다.
    moves: Tuple[Tuple[int, int], ...] = (
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    )

    while queue:
        row, col = queue.popleft()
        current_distance: int = visited[row][col]

        for dr, dc in moves:
            next_row, next_col = row + dr, col + dc

            # 체스판 범위를 벗어나면 무시한다.
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue

            # 처음 방문하는 칸이라면 이동 횟수를 기록한다.
            if visited[next_row][next_col] == -1:
                visited[next_row][next_col] = current_distance + 1

                # 목표에 도달하면 즉시 반환한다.
                if (next_row, next_col) == goal:
                    return visited[next_row][next_col]

                queue.append((next_row, next_col))

    raise ValueError("목표 지점에 도달할 수 없습니다.")


DETAILED_EXPLANATION = """
나이트 이동 문제는 각 칸을 노드로, 나이트가 한 번에 갈 수 있는 칸을 간선으로 생각하면 된다. 모든 간선이 동일한 비용을 가지므로 최단 거리 탐색에는 BFS가 적합하다. 큐에 시작 칸을 넣고 한 단계씩 확장하면서 이동 횟수를 기록하면, 특정 칸을 처음 방문할 때의 값이 항상 최소 이동 수이다. 목표 칸에 도달하면 그 값이 곧 정답이다. 이렇게 그래프로 추상화하고 BFS의 특성을 떠올리면 해결 전략을 쉽게 떠올릴 수 있다.
"""
