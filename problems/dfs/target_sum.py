"""
문제: 타겟 합 만들기

정수 배열과 목표 값이 주어진다. 배열의 각 원소 앞에 + 또는 - 부호를 붙여 모든 조합을 고려했을 때 목표 값을 만들 수 있는 경우의 수를 구하여라.

입력
첫째 줄에 배열의 길이 N(1 ≤ N ≤ 20)이 주어진다.
둘째 줄에 N개의 정수가 주어진다.
마지막 줄에 목표 값 T가 주어진다.

출력
가능한 경우의 수를 출력한다.

예제 입력 1
5
1 1 1 1 1
3

예제 출력 1
5

해설 요약
각 숫자에 +, -를 붙이는 두 가지 선택을 DFS로 탐색하며 누적 합을 추적하면 경우의 수를 셀 수 있다.
"""

from typing import Iterable, List


def count_target_sum(nums: Iterable[int], target: int) -> int:
    """DFS로 타겟 합을 만드는 경우의 수를 센다."""
    numbers: List[int] = list(nums)
    count = 0

    def dfs(index: int, total: int) -> None:
        nonlocal count

        if index == len(numbers):
            if total == target:
                count += 1
            return

        # 현재 숫자에 + 부호를 붙이는 선택
        dfs(index + 1, total + numbers[index])
        # 현재 숫자에 - 부호를 붙이는 선택
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)
    return count


DETAILED_EXPLANATION = """
각 숫자에 대해 + 또는 - 중 하나를 선택해야 하므로, 깊이 우선 탐색으로 모든 선택을 나열하면 경우의 수를 셀 수 있다. 재귀 함수는 현재 인덱스와 누적 합을 인자로 받고, 모든 숫자를 사용했을 때 누적 합이 목표와 같으면 정답을 하나 증가시킨다. 선택을 확장할 때는 +를 붙인 경우와 -를 붙인 경우를 각각 재귀 호출로 분기하면 된다. 이렇게 선택지를 트리 형태로 확장하는 사고방식이 DFS의 기본이다.
"""
