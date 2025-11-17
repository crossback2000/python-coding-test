# 실행: python 14.py < input.txt
"""
문제
수열의 모든 순열 생성
- 길이가 N인 서로 다른 정수 수열이 주어진다. 가능한 모든 순열을 사전식 순서와 관계없이 생성하여라.

입력
첫째 줄에 수열의 길이 N(1 ≤ N ≤ 8)이 주어진다.
둘째 줄에 N개의 서로 다른 정수가 주어진다.

출력
가능한 모든 순열을 한 줄에 하나씩 출력한다.

제한
1 ≤ N ≤ 8

예제
입력
3
1 2 3

출력
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

해설
사용하지 않은 숫자를 선택해 재귀적으로 자리를 채우는 DFS 백트래킹을 사용하면 모든 순열을 만들 수 있다.

"""

from typing import Iterable, List


def generate_permutations(nums: Iterable[int]) -> List[List[int]]:
    """백트래킹으로 모든 순열을 생성한다."""
    numbers = list(nums)
    used = [False] * len(numbers)
    current: List[int] = []
    result: List[List[int]] = []

    def dfs() -> None:
        if len(current) == len(numbers):
            result.append(current.copy())
            return

        for index, value in enumerate(numbers):
            if used[index]:
                continue

            # 아직 사용하지 않은 숫자를 선택한다.
            used[index] = True
            current.append(value)

            dfs()

            # 다른 순열을 위해 선택을 되돌린다.
            current.pop()
            used[index] = False

    dfs()
    return result


DETAILED_EXPLANATION = """
순열 문제는 한 자리에 올 수 있는 숫자를 하나씩 선택하면서 깊이를 내려가는 백트래킹 패턴으로 해결한다. 사용 여부를 배열로 관리하고, 숫자를 선택할 때마다 방문 표시를 해 중복 선택을 막는다. 모든 자리를 채우면 현재까지 만든 수열을 결과에 추가하고, 재귀가 끝나면 마지막 선택을 취소하여 다른 경우를 탐색한다. 이렇게 선택-되돌리기를 반복하는 사고 방식이 DFS 백트래킹의 핵심이다.
"""



def solve() -> None:
    """수열을 입력받아 가능한 모든 순열을 출력한다."""

    import sys

    input = sys.stdin.readline

    line = input().strip()
    if not line:
        return

    n = int(line)
    nums_line = input().strip()
    while nums_line == "":
        nums_line = input().strip()
    numbers = list(map(int, nums_line.split()))

    permutations = generate_permutations(numbers)
    output_lines = [" ".join(map(str, perm)) for perm in permutations]
    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    solve()
