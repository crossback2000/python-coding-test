# 실행: python 39.py < input.txt
"""
문제
배열 분할 최소 비용 (구간 DP + 누적합)
- 길이 N의 배열을 정확히 K개의 연속 구간으로 분할하고자 한다. 각 구간의 비용은 구간 합과 구간 길이의 곱으로 정의한다. 전체 비용의 합이 최소가 되도록 분할했을 때의 최소 비용을 구하라.

입력
첫째 줄에 N(1 ≤ N ≤ 500)과 K(1 ≤ K ≤ N)이 주어진다.
둘째 줄에 배열의 원소 a_i(0 ≤ a_i ≤ 10^9)가 공백으로 주어진다.

출력
최적 분할 시 총 비용의 최솟값을 출력한다.

제한
1 ≤ N ≤ 500 / 1 ≤ K ≤ N / 0 ≤ a_i ≤ 10^9

예제
입력
5 2
1 2 3 4 5

출력
45
설명: [1 2 3] | [4 5] 로 나누면 비용은 (6×3) + (9×2) = 18 + 27 = 45로 최소다.

해설
구간 합이 자주 필요하므로 prefix sum으로 O(1)에 구간 합을 계산하고, dp[i][k]를 "앞에서 i번째 원소까지 k개의 구간으로 자를 때 최소 비용"으로 정의한다. 마지막 구간의 시작점을 j로 가정해 dp[i][k] = min(dp[j-1][k-1] + cost(j, i))를 갱신한다.

"""

from typing import List


def min_partition_cost(nums: List[int], k: int) -> int:
    """구간 DP로 배열을 k개로 나눌 때의 최소 비용을 계산한다."""

    n = len(nums)
    prefix = [0] * (n + 1)
    for i, value in enumerate(nums, start=1):
        prefix[i] = prefix[i - 1] + value

    # 구간 합을 빠르게 계산하는 헬퍼 함수
    def range_sum(left: int, right: int) -> int:
        return prefix[right] - prefix[left - 1]

    INF = 10 ** 30
    dp = [[INF] * (k + 1) for _ in range(n + 1)]

    # 기본값: 첫 원소만 고려하고 구간 1개로 자를 때의 비용
    for i in range(1, n + 1):
        total = range_sum(1, i)
        dp[i][1] = total * i

    # 점화식을 이용해 구간 수를 늘려가며 갱신한다.
    for parts in range(2, k + 1):
        for end in range(parts, n + 1):
            # 마지막 구간의 시작점을 start로 설정
            for start in range(parts, end + 1):
                length = end - start + 1
                segment_sum = range_sum(start, end)
                cost = segment_sum * length
                candidate = dp[start - 1][parts - 1] + cost
                if candidate < dp[end][parts]:
                    dp[end][parts] = candidate

    return dp[n][k]


DETAILED_EXPLANATION = """
누적합 prefix[i] = a1 + ... + ai 를 만들면 임의의 구간 합은 O(1)이다. dp[end][parts]는
1..end 까지 parts개의 구간으로 나눌 때 최소 비용으로, 마지막 구간을 start..end라 가정하면
앞쪽(part-1개) 비용 dp[start-1][parts-1]과 마지막 구간 비용(segment_sum * length)을 더하면 된다.
모든 start를 시도해 최솟값을 택하면 된다. 시간 복잡도는 O(K * N^2)으로 N ≤ 500에서 감당 가능하다.
"""


def solve() -> None:
    """입력을 받아 배열 분할 최소 비용을 계산한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    n, k = map(int, line.split())
    nums = list(map(int, input().split()))
    print(min_partition_cost(nums, k))


if __name__ == "__main__":
    solve()
