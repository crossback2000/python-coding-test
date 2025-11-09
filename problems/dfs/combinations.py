"""
문제: 조합 생성하기

N개의 정수 중에서 정확히 K개를 선택하는 모든 조합을 사전식 순서와 관계없이 구하여라.

입력
첫째 줄에 정수 N과 K(1 ≤ K ≤ N ≤ 15)가 주어진다.
둘째 줄에 N개의 정수가 주어진다.

출력
모든 조합을 한 줄에 하나씩 출력한다.

예제 입력 1
4 2
1 2 3 4

예제 출력 1
1 2
1 3
1 4
2 3
2 4
3 4

해설 요약
현재까지 선택한 원소를 저장하고, 다음에 선택할 시작 위치를 넘겨주는 DFS를 사용하면 중복 없이 모든 조합을 만들 수 있다.
"""

from typing import Iterable, List


def generate_combinations(nums: Iterable[int], k: int) -> List[List[int]]:
    """DFS 백트래킹으로 크기 k 조합을 생성한다."""
    numbers = list(nums)
    result: List[List[int]] = []
    path: List[int] = []

    def dfs(start_index: int) -> None:
        if len(path) == k:
            result.append(path.copy())
            return

        for index in range(start_index, len(numbers)):
            # 현재 숫자를 선택하고 다음 숫자를 찾는다.
            path.append(numbers[index])
            dfs(index + 1)
            # 다른 조합을 위해 선택을 되돌린다.
            path.pop()

    dfs(0)
    return result


DETAILED_EXPLANATION = """
조합은 순서를 고려하지 않으므로, DFS를 진행할 때 다음에 탐색할 시작 위치를 함께 넘겨주면 중복을 피할 수 있다. 현재까지 선택한 원소가 K개가 되면 하나의 조합이 완성되므로 결과에 추가한다. 탐색이 끝나면 마지막으로 선택한 원소를 제거하여 다른 경우를 시도한다. 이런 방식으로 선택-되돌리기를 반복하면 모든 조합을 빠짐없이 생성할 수 있다.
"""



def solve() -> None:
    """정수 배열과 K를 입력받아 가능한 조합을 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, k = map(int, first_line.split())
    nums_line = input().strip()
    while nums_line == "":
        nums_line = input().strip()
    numbers = list(map(int, nums_line.split()))

    combinations = generate_combinations(numbers, k)
    output_lines = [" ".join(map(str, combo)) for combo in combinations]
    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    solve()
