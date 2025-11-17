"""
문제: 두 수의 합 구하기 (입출력 연습)

두 정수 A, B가 주어질 때 A + B를 출력한다. 가장 기본적인 입출력과
간단한 덧셈을 연습하기 위한 문제다.

입력
한 줄에 A와 B가 공백으로 구분되어 주어진다. (0 ≤ A, B ≤ 1_000)

출력
A + B를 한 줄에 출력한다.

예제 입력 1
1 2

예제 출력 1
3

해설 요약
정수 두 개를 읽어서 덧셈한 뒤 출력한다. 추가 자료구조가 필요 없으며,
표준 입력/출력 형식을 익히는 데 초점을 맞춘다.
"""


def add_two_numbers(a: int, b: int) -> int:
    """두 정수의 합을 반환한다."""

    return a + b


def solve() -> None:
    """표준 입력으로부터 두 수를 읽어 합을 출력한다."""

    import sys

    line = sys.stdin.readline().strip()
    if not line:
        return
    a, b = map(int, line.split())
    sys.stdout.write(str(add_two_numbers(a, b)))


if __name__ == "__main__":
    solve()
