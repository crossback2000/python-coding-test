# 실행: python 33.py < input.txt
"""
문제: 강의실 최소 개수 2 (우선순위 큐)

여러 강의의 시작 시각과 종료 시각이 주어질 때, 모든 강의를 겹치지 않게
배정하기 위해 필요한 최소 강의실 수를 구하라. 강의의 시작과 종료 시각은
정수이며, 종료 시각과 같은 시각에 다른 강의를 시작할 수 있다.

입력
첫째 줄에 강의의 개수 N(1 ≤ N ≤ 200,000)이 주어진다.
이후 N개의 줄에 시작 시각 s, 종료 시각 e(0 ≤ s < e ≤ 10^9)가 주어진다.

출력
필요한 최소 강의실의 수를 출력한다.

예제 입력 1
4
1 4
2 3
3 5
7 8

예제 출력 1
2

해설 요약
강의를 시작 시각 기준으로 정렬한 뒤, 현재 진행 중인 강의들의 종료 시각을
최소 힙에 저장한다. 새 강의의 시작 시각보다 먼저 끝나는 강의는 힙에서 제거하여
같은 강의실을 재사용하고, 힙의 크기가 동시에 필요한 강의실 수가 된다.
"""

import heapq
from typing import List, Tuple


def minimum_classrooms(intervals: List[Tuple[int, int]]) -> int:
    """우선순위 큐를 이용해 필요한 최소 강의실 수를 계산한다."""

    if not intervals:
        return 0

    # 1. 강의를 시작 시각 기준으로 정렬한다.
    intervals.sort(key=lambda x: x[0])

    # 2. 진행 중인 강의들의 종료 시각을 담을 최소 힙을 준비한다.
    min_heap: List[int] = []

    max_rooms = 0

    for start, end in intervals:
        # 3. 가장 빨리 끝나는 강의의 종료 시각이 현재 강의 시작 시각보다 작거나 같다면
        #    같은 강의실을 재사용할 수 있으므로 힙에서 제거한다.
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)

        # 4. 현재 강의의 종료 시각을 힙에 추가한다.
        heapq.heappush(min_heap, end)

        # 5. 순회 중에 동시에 필요한 최대 강의실 수를 추적한다.
        max_rooms = max(max_rooms, len(min_heap))

    # 힙에 남아 있는 원소의 최대 개수가 동시에 필요한 강의실 수이다.
    return max_rooms


DETAILED_EXPLANATION = """
시작 시각순으로 강의를 정렬하면, 각 강의가 시작될 때 이미 끝난 강의실만 비어 있다.
진행 중인 강의의 종료 시각을 최소 힙으로 관리하면, 가장 빨리 끝나는 강의부터 확인할 수 있다.
새 강의의 시작 시각보다 종료 시각이 작거나 같은 항목을 힙에서 꺼내면 해당 강의실을 재사용한다.
모든 강의에 대해 이 과정을 반복한 뒤 힙의 크기가 곧 필요한 강의실 수다. 정렬 O(N log N)과 힙 연산
O(N log N)으로 전체 시간 복잡도는 O(N log N)이다.
"""


def solve() -> None:
    """입력을 받아 최소 강의실 수를 계산한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    n = int(line)
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    print(minimum_classrooms(intervals))


if __name__ == "__main__":
    solve()
