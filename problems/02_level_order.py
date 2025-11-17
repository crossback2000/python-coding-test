"""
문제: 이진 트리의 레벨 순회 결과

이진 트리가 주어졌을 때, 루트부터 시작하여 레벨별로 노드 값을 순서대로 출력해라. 같은 레벨의 노드는 왼쪽에서 오른쪽 순서로 나열한다.

입력
첫째 줄에 노드 수 N(1 ≤ N ≤ 10,000)이 주어진다. 이후 N개의 줄에는 노드 값과 왼쪽 자식, 오른쪽 자식 인덱스가 주어진다. 자식이 없으면 -1로 표시한다. 0번 노드가 루트다.

출력
레벨 순서대로 각 레벨의 노드 값을 공백으로 구분하여 출력한다. 레벨이 바뀌면 줄을 바꾼다.

예제 입력 1
5
3 1 2
9 -1 -1
20 3 4
15 -1 -1
7 -1 -1

예제 출력 1
3
9 20
15 7

해설 요약
큐를 사용해 레벨 단위로 BFS를 수행하면, 같은 레벨에 있는 노드를 한 번에 처리하면서 원하는 출력 순서를 얻을 수 있다.
"""

from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    """이진 트리 노드 구조."""

    __slots__ = ("value", "left", "right")

    def __init__(
        self,
        value: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def level_order_values(root: Optional[TreeNode]) -> List[List[int]]:
    """루트에서 시작해 레벨별 노드 값을 2차원 리스트로 반환한다."""
    if root is None:
        return []

    result: List[List[int]] = []
    queue: Deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        current_level: List[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(current_level)

    return result


DETAILED_EXPLANATION = """
이 문제는 트리를 레벨별로 순회하는 전형적인 BFS 패턴이다. 큐에 루트 노드를 넣고, 현재 큐 크기만큼 노드를 꺼내며 같은 레벨을 묶어 저장한다. 자식 노드는 다음 레벨을 위해 큐에 추가한다. 이렇게 반복하면 레벨 순서가 자연스럽게 유지되고, 각 레벨의 값을 차례대로 기록할 수 있다. BFS가 레벨 단위 탐색에 적합하다는 사실을 기억하면 쉽게 접근할 수 있다.
"""



def solve() -> None:
    """표준 입력으로 이진 트리를 받아 레벨 순회 결과를 출력한다."""

    import sys

    input = sys.stdin.readline

    line = input().strip()
    if not line:
        return

    n = int(line)
    nodes = []
    children = []
    for _ in range(n):
        node_line = input().strip()
        while node_line == "":
            node_line = input().strip()
        value, left, right = map(int, node_line.split())
        nodes.append(TreeNode(value))
        children.append((left, right))

    for index, (left, right) in enumerate(children):
        if left != -1:
            nodes[index].left = nodes[left]
        if right != -1:
            nodes[index].right = nodes[right]

    levels = level_order_values(nodes[0] if nodes else None)
    output_lines = [" ".join(map(str, level)) for level in levels]
    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    solve()
