# 실행: python 09.py < input.txt
"""
문제
원하는 값의 위치 찾기
- 정수 배열과 찾고 싶은 값 X가 주어질 때, X가 등장하는 첫 번째 인덱스를 출력한다. (0-based) 존재하지 않으면 -1을 출력한다.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 100)과 찾을 값 X가 공백으로 주어진다.
둘째 줄에 N개의 정수가 주어진다.

출력
X가 처음 나타나는 인덱스 또는 -1을 출력한다.

제한
1 ≤ N ≤ 100

예제
입력
6 5
1 3 5 7 5 9

출력
2

해설
왼쪽부터 순차적으로 확인하며 X를 만나면 즉시 인덱스를 반환한다. 마지막까지 없으면 -1을 출력한다.

"""

from typing import Iterable


def find_first_index(numbers: Iterable[int], target: int) -> int:
    """타깃이 처음 등장하는 위치를 반환한다 (없으면 -1)."""

    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1


def solve() -> None:
    """배열과 타깃을 입력받아 첫 등장 위치를 출력한다."""

    import sys

    input = sys.stdin.readline
    first = input().strip()
    if not first:
        return
    n, target = map(int, first.split())
    values = list(map(int, input().split()))[:n]
    sys.stdout.write(str(find_first_index(values, target)))


if __name__ == "__main__":
    solve()
