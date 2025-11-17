# 실행: python 05.py < input.txt
"""
문제: 문자열 뒤집기

소문자로만 이루어진 문자열 S가 주어질 때, 역순으로 뒤집어 출력한다.
슬라이싱을 활용한 문자열 조작 연습 문제다.

입력
첫째 줄에 문자열 S가 주어진다. (1 ≤ |S| ≤ 100)

출력
문자열을 뒤집어 한 줄에 출력한다.

예제 입력 1
hello

예제 출력 1
olleh

해설 요약
파이썬 슬라이싱 ``s[::-1]``을 사용하면 한 줄로 뒤집을 수 있다.
반복문으로 문자를 앞에서부터 누적해도 정답이다.
"""


def reverse_string(s: str) -> str:
    """문자열을 역순으로 뒤집어 반환한다."""

    return s[::-1]


def solve() -> None:
    """입력 문자열을 뒤집어 출력한다."""

    import sys

    s = sys.stdin.readline().strip()
    if not s:
        return
    sys.stdout.write(reverse_string(s))


if __name__ == "__main__":
    solve()
