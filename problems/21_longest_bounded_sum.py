"""
문제: 부분합이 제한된 가장 긴 구간 찾기 (슬라이딩 윈도우)

N개의 비음수 정수와 합의 상한 S가 주어진다. 연속 부분배열 중 원소의
합이 S 이하인 가장 긴 길이를 구하여라. 조건을 만족하는 구간이 여러 개라면
길이만 출력하면 된다.

입력
첫째 줄에 N(1 ≤ N ≤ 200,000)과 S(0 ≤ S ≤ 10^12)가 주어진다.
둘째 줄에 배열의 원소 a_1, a_2, ... , a_N(0 ≤ a_i ≤ 10^9)이 공백으로 주어진다.

출력
합이 S 이하인 가장 긴 연속 부분배열의 길이를 출력한다.

예제 입력 1
5 5
1 2 3 2 1

예제 출력 1
2

설명: 합이 5 이하인 가장 긴 구간은 [3, 2] 또는 [2, 1] 등 길이 2인 구간들이다.

해설 요약
모든 숫자가 음이 아니므로, 왼쪽과 오른쪽 포인터를 움직이는 슬라이딩 윈도우로
현재 구간의 합을 유지하며 길이가 조건을 넘는 순간 왼쪽 포인터를 이동시켜
합을 줄인다. 모든 원소를 한 번씩만 이동시키므로 O(N) 시간에 답을 구할 수 있다.
"""

from typing import List


def longest_subarray_at_most_sum(nums: List[int], limit: int) -> int:
    """합이 limit 이하인 가장 긴 연속 부분배열 길이를 반환한다."""

    # 현재 윈도우의 합과 가장 긴 길이를 기록한다.
    window_sum = 0
    max_length = 0
    left = 0

    # 오른쪽 포인터를 한 칸씩 늘리며 윈도우를 확장한다.
    for right, value in enumerate(nums):
        window_sum += value

        # 윈도우 합이 제한을 초과하면 왼쪽 포인터를 이동시켜 합을 줄인다.
        # 모든 값이 비음수이므로 왼쪽을 이동할수록 합이 감소한다.
        while window_sum > limit and left <= right:
            window_sum -= nums[left]
            left += 1

        # 제한을 만족하는 상태에서 윈도우 길이를 갱신한다.
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length


DETAILED_EXPLANATION = """
두 포인터를 이용한 슬라이딩 윈도우는 비음수 수열의 연속 합 제약 문제에 최적이다.
왼쪽과 오른쪽 인덱스를 윈도우의 경계로 두고, 오른쪽을 한 칸씩 이동하며 합을 누적한다.
합이 상한을 넘는 순간, 왼쪽을 이동시키며 초과분을 제거하면 된다. 각 인덱스는 왼쪽과 오른쪽
포인터로 최대 한 번씩만 이동하므로 전체 시간 복잡도는 O(N)이다. 추가 메모리는 상수다.
"""


def solve() -> None:
    """입력을 받아 슬라이딩 윈도우로 답을 출력한다."""

    import sys

    input = sys.stdin.readline

    line = input().strip()
    if not line:
        return

    n, limit = map(int, line.split())
    nums = list(map(int, input().split()))
    print(longest_subarray_at_most_sum(nums, limit))


if __name__ == "__main__":
    solve()
