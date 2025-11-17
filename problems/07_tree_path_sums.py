"""
문제: 이진 트리 경로 합

이진 트리의 각 노드에는 정수가 적혀 있다. 루트에서 리프까지 내려가는 모든 경로에 대해 노드 값의 합을 구하여라.

입력
첫째 줄에 노드 수 N(1 ≤ N ≤ 10,000)이 주어진다.
이후 N개의 줄에는 노드 값과 왼쪽, 오른쪽 자식의 인덱스가 주어진다. 자식이 없으면 -1이다. 0번 노드가 루트다.

출력
각 루트-리프 경로의 합을 한 줄에 하나씩 출력한다.

예제 입력 1
5
5 1 2
4 3 4
8 -1 -1
11 -1 -1
13 -1 -1

예제 출력 1
20
22
26

해설 요약
DFS로 루트에서 리프까지 내려가면서 누적 합을 전달하면 모든 경로의 합을 구할 수 있다.
"""

from typing import List, Optional


class TreeNode:
    """이진 트리 노드를 표현하는 경량 클래스."""

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


def binary_tree_path_sums(root: Optional[TreeNode]) -> List[int]:
    """DFS로 루트에서 리프까지의 경로 합을 모두 구한다."""
    if root is None:
        return []

    sums: List[int] = []

    def dfs(node: TreeNode, current_sum: int) -> None:
        new_sum = current_sum + node.value

        if node.left is None and node.right is None:
            sums.append(new_sum)
            return

        if node.left is not None:
            dfs(node.left, new_sum)
        if node.right is not None:
            dfs(node.right, new_sum)

    dfs(root, 0)
    return sums


DETAILED_EXPLANATION = """
트리에서 루트부터 리프까지 내려가며 누적 합을 기록하면 각 경로의 합을 구할 수 있다. 재귀 함수는 현재 노드와 누적 합을 인자로 받고, 리프를 만나면 누적 합을 결과에 추가한다. 리프가 아니면 왼쪽과 오른쪽 자식으로 내려가면서 현재까지의 합을 전달한다. 이런 방식으로 DFS가 경로마다 독립적으로 합을 계산하게 된다. 트리를 따라가며 값을 누적하는 문제에서 자주 사용하는 패턴이다.
"""



def solve() -> None:
    """이진 트리 입력을 받아 모든 루트-리프 경로 합을 출력한다."""

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

    sums = binary_tree_path_sums(nodes[0] if nodes else None)
    sys.stdout.write("\n".join(str(total) for total in sums))


if __name__ == "__main__":
    solve()
