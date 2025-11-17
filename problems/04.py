# 실행: python 04.py < input.txt
"""
문제: 인접 원소 최소 차이

정수 배열에서 서로 이웃한 두 원소의 차이(절댓값) 중 가장 작은 값을 구한다.
반복문과 기본적인 갱신 패턴을 연습할 수 있다.

입력
첫째 줄에 정수 N (2 ≤ N ≤ 100)이 주어진다.
둘째 줄에 N개의 정수가 공백으로 주어진다.

출력
인접한 두 수의 절댓값 차이 중 최솟값을 출력한다.

예제 입력 1
5
5 4 8 6 7

예제 출력 1
1

해설 요약
왼쪽부터 오른쪽으로 순회하며 이전 원소와의 차이를 계산해 최솟값을
갱신한다. O(N)으로 해결된다.
"""

from typing import Iterable


def min_adjacent_diff(numbers: Iterable[int]) -> int:
    """인접 원소 간 절댓값 차이의 최솟값을 반환한다."""

    iterator = iter(numbers)
    try:
        prev = next(iterator)
    except StopIteration:  # pragma: no cover - 방어 로직
        raise ValueError("numbers must contain at least one element")

    min_diff = float("inf")
    for current in iterator:
        min_diff = min(min_diff, abs(current - prev))
        prev = current
    return int(min_diff)


def solve() -> None:
    """배열을 입력받아 인접 원소 최소 차이를 출력한다."""

    import sys

    input = sys.stdin.readline
    first_line = input().strip()
    if not first_line:
        return
    n = int(first_line)
    values = list(map(int, input().split()))[:n]
    sys.stdout.write(str(min_adjacent_diff(values)))


if __name__ == "__main__":
    solve()
