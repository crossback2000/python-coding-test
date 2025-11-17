# 실행: python 08.py < input.txt
"""
문제: 누적 합 출력하기

N개의 정수가 주어질 때, 앞에서부터의 누적 합을 공백으로 출력한다.
반복문과 누적 변수 사용을 익히기 위한 문제다.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄에 N개의 정수가 공백으로 주어진다.

출력
누적 합을 담은 수열을 공백으로 구분해 한 줄에 출력한다.

예제 입력 1
5
1 2 3 4 5

예제 출력 1
1 3 6 10 15

해설 요약
현재까지의 합을 저장하는 변수를 두고, 각 원소를 더하면서 결과 리스트에
추가한다.
"""

from typing import Iterable, List


def running_total(numbers: Iterable[int]) -> List[int]:
    """왼쪽부터의 누적 합 배열을 반환한다."""

    total = 0
    result: List[int] = []
    for value in numbers:
        total += value
        result.append(total)
    return result


def solve() -> None:
    """수열을 입력받아 누적 합을 공백으로 출력한다."""

    import sys

    input = sys.stdin.readline
    first_line = input().strip()
    if not first_line:
        return
    n = int(first_line)
    values = list(map(int, input().split()))[:n]
    prefix = running_total(values)
    sys.stdout.write(" ".join(map(str, prefix)))


if __name__ == "__main__":
    solve()
