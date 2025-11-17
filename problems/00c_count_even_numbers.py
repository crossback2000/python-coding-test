"""
문제: 짝수 개수 세기

N개의 정수가 주어질 때, 그중 짝수의 개수를 출력한다.
리스트 순회와 조건 판별을 연습하는 입문 문제다.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄에 N개의 정수가 공백으로 구분되어 주어진다.

출력
짝수의 개수를 한 줄에 출력한다.

예제 입력 1
5
1 2 3 4 5

예제 출력 1
2

해설 요약
모든 숫자를 순회하며 2로 나누어 떨어지는지 확인하고, 참이면 카운터를
증가시킨다. 조건문과 for 반복문만으로 해결된다.
"""

from typing import Iterable


def count_even_numbers(numbers: Iterable[int]) -> int:
    """리스트에 포함된 짝수의 개수를 반환한다."""

    return sum(1 for value in numbers if value % 2 == 0)


def solve() -> None:
    """입력된 수열에서 짝수 개수를 세어 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return
    n = int(first_line)
    values = list(map(int, input().split()))
    values = values[:n]
    sys.stdout.write(str(count_even_numbers(values)))


if __name__ == "__main__":
    solve()
