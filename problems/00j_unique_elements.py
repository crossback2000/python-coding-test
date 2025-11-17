"""
문제: 중복 제거하기

정수 배열이 주어질 때, 등장 순서를 유지하며 중복되지 않는 원소만
출력한다. 집합과 리스트를 함께 사용하는 기초적인 자료구조 문제다.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄에 N개의 정수가 공백으로 주어진다.

출력
중복을 제거한 수열을 공백으로 출력한다.

예제 입력 1
7
1 3 3 2 5 1 2

예제 출력 1
1 3 2 5

해설 요약
이미 본 숫자를 집합에 기록하면서, 처음 등장한 숫자만 결과 리스트에
추가한다. 입력 크기가 작아도 기본적인 "방문 기록" 패턴을 익힐 수 있다.
"""

from typing import Iterable, List


def unique_preserve_order(numbers: Iterable[int]) -> List[int]:
    """등장 순서를 유지하며 중복 없는 리스트를 반환한다."""

    seen: set[int] = set()
    result: List[int] = []
    for value in numbers:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def solve() -> None:
    """수열을 입력받아 중복을 제거한 결과를 출력한다."""

    import sys

    input = sys.stdin.readline
    first_line = input().strip()
    if not first_line:
        return
    n = int(first_line)
    values = list(map(int, input().split()))[:n]
    deduped = unique_preserve_order(values)
    sys.stdout.write(" ".join(map(str, deduped)))


if __name__ == "__main__":
    solve()
