# 실행: python 34.py < input.txt
"""
문제: 최소 회문 분할 (DP + 전처리)

문자열을 여러 조각으로 나누어 각 조각이 회문이 되도록 할 때, 필요한 최소 분할 횟수를 구하라.
분할 횟수는 조각의 개수 - 1 로 정의한다. 빈 문자열은 주어지지 않는다.

입력
첫째 줄에 길이 L(1 ≤ L ≤ 2,000)의 문자열이 주어진다. 문자열은 소문자로만 구성된다.

출력
모든 부분 문자열이 회문이 되도록 하는 최소 분할 횟수를 출력한다.

예제 입력 1
abccbc

예제 출력 1
2

설명: "a | bccb | c" 와 같이 세 조각으로 나누면 모두 회문이며, 분할 횟수는 2이다.

해설 요약
회문 여부를 빠르게 확인하기 위해 모든 구간 [i, j]가 회문인지 O(L^2) 전처리한다.
이후 dp[i]를 0..i 구간을 회문들로 덮을 때 필요한 최소 분할 횟수로 정의하면,
최종 답은 dp[L-1]이다. 각 위치에서 가능한 회문 시작점을 확인하며 최솟값을 갱신한다.
"""

from typing import List


def preprocess_palindrome(s: str) -> List[List[bool]]:
    """모든 구간이 회문인지 여부를 O(n^2)에 미리 계산한다."""

    n = len(s)
    is_pal = [[False] * n for _ in range(n)]

    # 길이 1인 구간은 모두 회문이다.
    for i in range(n):
        is_pal[i][i] = True

    # 길이 2 이상인 구간을 확장 길이 기준으로 채운다.
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end]:
                if length == 2:
                    # 길이 2인 경우 양 끝만 비교하면 된다.
                    is_pal[start][end] = True
                else:
                    # 양 끝이 같고 내부 구간이 회문이면 전체도 회문이다.
                    is_pal[start][end] = is_pal[start + 1][end - 1]
    return is_pal


def min_palindrome_cut(s: str) -> int:
    """문자열을 회문으로 자를 때 필요한 최소 분할 횟수를 반환한다."""

    n = len(s)
    is_pal = preprocess_palindrome(s)

    # dp[i]: s[0..i]를 회문들로 분할할 때 필요한 최소 분할 횟수
    dp = [0] * n

    for end in range(n):
        # s[0..end] 자체가 회문이면 분할이 필요 없다.
        if is_pal[0][end]:
            dp[end] = 0
            continue

        # 아니라면, 중간 지점을 나누어 최소 분할 값을 찾는다.
        min_cuts = end  # 최악의 경우 매 문자마다 자른다.
        for start in range(1, end + 1):
            if is_pal[start][end]:
                # s[start..end]가 회문이면, 그 앞부분 dp[start-1]에 +1 분할을 한다.
                min_cuts = min(min_cuts, dp[start - 1] + 1)
        dp[end] = min_cuts
    return dp[-1]


DETAILED_EXPLANATION = """
회문 판정이 O(1)이어야 전체가 효율적이다. is_pal[start][end]를 채우기 위해 길이를 1에서 n까지 확장하며
양 끝 문자가 같고 내부 구간이 회문인지 확인한다. 이후 dp[end]를 계산할 때 end에서 끝나는 모든 회문 구간을
확인하며 최솟값을 고른다. 전처리가 O(n^2), DP 역시 O(n^2)로 총 시간 복잡도는 O(n^2)이며, 추가 메모리도 O(n^2)이다.
"""


def solve() -> None:
    """입력을 받아 최소 회문 분할 횟수를 계산한다."""

    import sys

    s = sys.stdin.readline().strip()
    if not s:
        return

    print(min_palindrome_cut(s))


if __name__ == "__main__":
    solve()
