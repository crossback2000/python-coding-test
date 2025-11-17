"""
문제: 팰린드롬 판별

문자열 S가 앞뒤가 같은 팰린드롬인지 확인하여 "YES" 또는 "NO"를 출력한다.
대소문자는 구분하지 않는다.

입력
첫째 줄에 문자열 S가 주어진다. (1 ≤ |S| ≤ 100)

출력
S가 팰린드롬이면 "YES", 아니면 "NO"를 출력한다.

예제 입력 1
Level

예제 출력 1
YES

해설 요약
모두 소문자로 바꾼 뒤 뒤집은 문자열과 비교하면 간단히 판별할 수 있다.
"""


def is_palindrome(text: str) -> bool:
    """대소문자를 무시하고 팰린드롬 여부를 반환한다."""

    lowered = text.lower()
    return lowered == lowered[::-1]


def solve() -> None:
    """문자열의 팰린드롬 여부를 판정해 출력한다."""

    import sys

    s = sys.stdin.readline().strip()
    if not s:
        return
    sys.stdout.write("YES" if is_palindrome(s) else "NO")


if __name__ == "__main__":
    solve()
