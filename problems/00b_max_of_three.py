"""
문제: 세 수 중 최댓값 찾기

세 정수 A, B, C가 주어질 때 가장 큰 값을 출력한다.
조건문 사용과 비교 연산을 익히기 위한 쉬운 연습 문제다.

입력
한 줄에 세 정수 A, B, C가 공백으로 주어진다. (-1_000 ≤ A, B, C ≤ 1_000)

출력
세 수 중 최댓값을 한 줄에 출력한다.

예제 입력 1
3 7 5

예제 출력 1
7

해설 요약
내장 함수 ``max``를 사용하거나, 비교 연산으로 직접 갱신해도 된다.
여기서는 로직을 읽기 쉽게 max 함수를 사용한다.
"""

from typing import Iterable


def max_of_three(values: Iterable[int]) -> int:
    """세 정수의 최댓값을 반환한다."""

    a, b, c = values
    return max(a, b, c)


def solve() -> None:
    """세 수를 입력받아 최댓값을 출력한다."""

    import sys

    line = sys.stdin.readline().strip()
    if not line:
        return
    numbers = tuple(map(int, line.split()))
    if len(numbers) != 3:  # pragma: no cover - 잘못된 입력 방어
        return
    sys.stdout.write(str(max_of_three(numbers)))


if __name__ == "__main__":
    solve()
