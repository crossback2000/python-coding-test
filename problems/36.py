# 실행: python 36.py < input.txt
"""
문제
실시간 구간 합 질의 (펜윅 트리)
- N개의 정수 배열이 주어지고, 두 가지 연산을 처리해야 한다. 1) "1 idx val" : idx 위치의 값을 val로 갱신한다. 2) "2 l r" : 구간 [l, r]의 합을 출력한다. 연산은 총 Q번 주어지며, 1 ≤ idx, l, r ≤ N 이다.

입력
첫째 줄에 N(1 ≤ N ≤ 200,000)과 Q(1 ≤ Q ≤ 200,000)이 주어진다.
둘째 줄에 초기 배열의 값이 주어지고, 이후 Q개의 연산이 한 줄에 하나씩 주어진다.

출력
모든 2번 연산의 결과를 순서대로 출력한다.

제한
1 ≤ N ≤ 200,000 / 1 ≤ Q ≤ 200,000

예제
입력
5 5
1 2 3 4 5
2 1 5
1 3 10
2 2 4
1 5 -2
2 3 5

출력
15
16
12

해설
배열이 크고 갱신과 질의가 번갈아 등장하므로, O(log N)에 갱신과 합 계산이 가능한 펜윅 트리(BIT)를 사용한다. 각 노드가 담당하는 구간 길이가 2의 거듭제곱이므로, 인덱스를 비트 연산으로 이동시키며 빠르게 합을 갱신/조회할 수 있다.

"""

from typing import List


class FenwickTree:
    """1-based 펜윅 트리 구현."""

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def _lsb(self, index: int) -> int:
        """가장 낮은 비트를 반환 (해당 노드가 담당하는 구간 길이)."""

        return index & -index

    def update(self, index: int, delta: int) -> None:
        """index 위치에 delta를 더한다."""

        while index <= self.size:
            self.tree[index] += delta
            index += self._lsb(index)

    def query(self, index: int) -> int:
        """1..index 구간의 누적 합을 반환한다."""

        result = 0
        while index > 0:
            result += self.tree[index]
            index -= self._lsb(index)
        return result

    def range_sum(self, left: int, right: int) -> int:
        """구간 [left, right]의 합을 반환한다."""

        return self.query(right) - self.query(left - 1)


def dynamic_range_sum(nums: List[int], operations: List[List[int]]) -> List[int]:
    """주어진 연산들을 처리하며 모든 구간 합 답을 리스트로 반환한다."""

    n = len(nums)
    bit = FenwickTree(n)

    # 초기 배열을 트리에 반영한다.
    for idx, value in enumerate(nums, start=1):
        bit.update(idx, value)

    outputs: List[int] = []

    for op in operations:
        if op[0] == 1:
            _, idx, new_val = op
            # 현재 값을 알아내기 위해 구간 합 차이를 이용한다.
            current = bit.range_sum(idx, idx)
            bit.update(idx, new_val - current)
        else:
            _, l, r = op
            outputs.append(bit.range_sum(l, r))

    return outputs


DETAILED_EXPLANATION = """
펜윅 트리는 부분합을 빠르게 다루기 위한 자료구조다. update는 해당 인덱스의 값을 포함하는 모든 상위 노드에 delta를 더한다.
query는 인덱스를 낮추며 필요한 노드의 값을 누적한다. 각 단계에서 인덱스를 lsb만큼 이동하므로 O(log N) 시간에 끝난다.
초기 배열을 트리에 빌드한 뒤, 점 갱신과 구간 합을 번갈아 처리해도 전체 시간은 Q log N에 수렴한다.
"""


def solve() -> None:
    """입력을 받아 펜윅 트리로 연산을 처리한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    n, q = map(int, line.split())
    nums = list(map(int, input().split()))

    operations: List[List[int]] = []
    for _ in range(q):
        operations.append(list(map(int, input().split())))

    results = dynamic_range_sum(nums, operations)
    sys.stdout.write("\n".join(map(str, results)))


if __name__ == "__main__":
    solve()
