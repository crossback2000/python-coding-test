"""
문제: 이진 트리의 최소 깊이

이진 트리가 주어졌을 때, 루트 노드에서 가장 가까운 리프 노드까지의 최소 깊이를 구하여라. 깊이는 루트에서 리프까지 지나온 노드의 수를 의미한다.

입력
첫째 줄에 노드의 수 N(1 ≤ N ≤ 10,000)이 주어진다. 이후 N개의 줄에 걸쳐 각 노드의 값과 왼쪽 자식, 오른쪽 자식의 인덱스가 주어진다. -1은 자식이 없음을 의미한다. 노드 인덱스는 0부터 N-1까지이며, 0번 노드가 루트이다.

출력
루트에서 가장 가까운 리프 노드까지의 최소 깊이를 출력한다.

예제 입력 1
5
3 1 2
9 -1 -1
20 3 4
15 -1 -1
7 -1 -1

예제 출력 1
2

해설 요약
루트부터 레벨 순회로 BFS를 수행하면서 처음으로 리프 노드를 만나는 순간의 깊이가 최소 깊이가 된다.
"""

from collections import deque
from typing import Deque, Optional, Tuple


class TreeNode:
    """이진 트리 노드를 표현하는 자료구조."""

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


def minimum_depth(root: Optional[TreeNode]) -> int:
    """루트에서 가장 가까운 리프 노드까지의 깊이를 구한다."""
    if root is None:
        return 0

    # 노드와 현재 깊이를 함께 큐에 넣고 BFS를 수행한다.
    queue: Deque[Tuple[TreeNode, int]] = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        # 리프 노드를 만나면 그 깊이가 최소 깊이다.
        if node.left is None and node.right is None:
            return depth

        # 왼쪽 자식이 있다면 큐에 추가하며 깊이를 1 증가시킨다.
        if node.left is not None:
            queue.append((node.left, depth + 1))

        # 오른쪽 자식도 같은 방식으로 처리한다.
        if node.right is not None:
            queue.append((node.right, depth + 1))

    return 0


DETAILED_EXPLANATION = """
이진 트리의 최소 깊이는 루트에서 가장 가까운 리프까지의 거리다. 모든 간선의 비용이 1이므로, 루트부터 너비 우선 탐색을 진행하면 레벨별로 노드를 방문하게 된다. 따라서 BFS 중 가장 먼저 만나는 리프 노드가 곧 최소 깊이를 가진다. 문제를 트리를 그래프로 바라보고, 리프를 만나는 순간 탐색을 종료한다는 전략을 세우면 자연스럽게 풀이가 완성된다.
"""



def solve() -> None:
    """이진 트리 입력을 받아 최소 깊이를 출력한다."""

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

    print(minimum_depth(nodes[0] if nodes else None))


if __name__ == "__main__":
    solve()
