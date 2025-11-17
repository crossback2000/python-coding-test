# 실행: python 32.py < input.txt
"""
문제: 2차원 구간합 질의 (누적합 전처리)

N×N 격자에 정수가 채워져 있을 때, Q개의 직사각형 구간합 질의를 처리하라.
각 질의는 (r1, c1)에서 (r2, c2)까지의 좌상단/우하단 좌표가 주어지며,
해당 영역의 모든 원소 합을 출력해야 한다. 좌표는 1부터 시작한다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000)과 Q(1 ≤ Q ≤ 100,000)이 주어진다.
이후 N개의 줄에 격자의 값이 주어지고, 이어서 Q개의 줄에 네 정수 r1, c1, r2, c2가 주어진다.

출력
각 질의에 대한 구간합을 한 줄에 하나씩 출력한다.

예제 입력 1
4 3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1 1 2 2
2 2 3 4
1 1 4 4

예제 출력 1
14
54
136

해설 요약
한 번의 전처리로 2차원 누적합을 구하면, 모든 구간합을 O(1) 시간에 답할 수 있다.
누적합 ps[r][c]는 (1,1)부터 (r,c)까지의 합을 의미하므로, 임의의 직사각형 합은
포함-배제 원리를 이용해 상수 시간에 계산된다.
"""

from typing import List


def build_prefix_sum(grid: List[List[int]]) -> List[List[int]]:
    """격자에 대한 2차원 누적합 테이블을 생성한다."""

    n = len(grid)
    # 편의를 위해 (n+1)×(n+1) 크기의 배열을 만들어 1-based 누적합을 저장한다.
    prefix = [[0] * (n + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            # 현재 위치까지의 합은
            # 위쪽 누적합 + 왼쪽 누적합 - 대각선 중복 + 현재 값 으로 계산한다.
            prefix[r][c] = (
                prefix[r - 1][c]
                + prefix[r][c - 1]
                - prefix[r - 1][c - 1]
                + grid[r - 1][c - 1]
            )
    return prefix


def query_sum(prefix: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
    """누적합 표를 활용해 직사각형 합을 상수 시간에 구한다."""

    # 포함-배제: 전체 사각형 - 위쪽 띠 - 왼쪽 띠 + 겹친 대각선 영역
    return (
        prefix[r2][c2]
        - prefix[r1 - 1][c2]
        - prefix[r2][c1 - 1]
        + prefix[r1 - 1][c1 - 1]
    )


DETAILED_EXPLANATION = """
2차원 누적합은 특정 좌표까지의 부분합을 저장한다. ps[r][c] = (1,1)부터 (r,c)까지의 합이라면,
(r1,c1)-(r2,c2)의 합은 ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]이다.
모든 질의를 처리하는 동안 O(1) 시간만 사용하고, 전처리는 O(N^2)만 필요하다. 추가 메모리는 (N+1)^2이다.
"""


def solve() -> None:
    """입력을 받아 누적합을 만들고 질의를 처리한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    n, q = map(int, line.split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    prefix = build_prefix_sum(grid)

    outputs = []
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        outputs.append(str(query_sum(prefix, r1, c1, r2, c2)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
