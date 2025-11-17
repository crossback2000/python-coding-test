# 실행: python 07.py < input.txt
"""
문제
모음 개수 세기
- 영문 소문자 문자열이 주어질 때, 모음(a, e, i, o, u)의 개수를 출력한다. 간단한 집합 membership 연산을 연습한다.

입력
첫째 줄에 문자열 S가 주어진다. (1 ≤ |S| ≤ 200)

출력
문자열 S에 포함된 모음의 총 개수를 출력한다.

제한
1 ≤ |S| ≤ 200

예제
입력
kotlin

출력
2

해설
모음 집합을 만들어 각 문자가 집합에 속하는지 확인하며 카운트한다.

"""


VOWELS = {"a", "e", "i", "o", "u"}


def count_vowels(text: str) -> int:
    """소문자 문자열에 포함된 모음 개수를 반환한다."""

    return sum(1 for ch in text if ch in VOWELS)


def solve() -> None:
    """문자열을 입력받아 모음 개수를 출력한다."""

    import sys

    s = sys.stdin.readline().strip()
    if not s:
        return
    sys.stdout.write(str(count_vowels(s)))


if __name__ == "__main__":
    solve()
