"""
문제: 방향 비순환 그래프의 모든 경로 구하기

방향 비순환 그래프(DAG)가 인접 리스트 형태로 주어진다. 시작 정점 0에서 마지막 정점 N-1까지 도달할 수 있는 모든 경로를 찾아라.

입력
첫째 줄에 정점 수 N(2 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 각 정점에서 나가는 간선 정보가 주어진다. i번째 줄에는 정점 i에서 이동할 수 있는 정점 번호가 공백으로 구분되어 주어진다. 이동할 수 있는 정점이 없다면 빈 줄이 주어진다.

출력
시작 정점 0에서 정점 N-1까지의 모든 경로를 한 줄에 하나씩 출력한다.

예제 입력 1
4
1 2
3
3

예제 출력 1
0 1 3
0 2 3

해설 요약
DFS로 현재까지의 경로를 저장하면서 목적지에 도달할 때마다 경로를 기록하면 모든 경로를 찾을 수 있다.
"""

from typing import Iterable, List


def enumerate_all_paths(graph: Iterable[Iterable[int]]) -> List[List[int]]:
    """DFS로 시작 정점에서 도착 정점까지의 모든 경로를 나열한다."""
    adjacency: List[List[int]] = [list(neighbors) for neighbors in graph]
    target = len(adjacency) - 1
    path: List[int] = [0]
    result: List[List[int]] = []

    def dfs(node: int) -> None:
        if node == target:
            result.append(path.copy())
            return

        for neighbor in adjacency[node]:
            path.append(neighbor)
            dfs(neighbor)
            path.pop()

    dfs(0)
    return result


DETAILED_EXPLANATION = """
DAG에서 모든 경로를 찾으려면 현재까지 지나온 노드를 기억하면서 깊이 우선 탐색을 수행하면 된다. 각 노드에서 나갈 수 있는 이웃을 순서대로 방문하고, 목적지에 도달하면 지금까지 저장된 경로를 결과에 추가한다. 탐색을 마친 뒤에는 되돌아가면서 마지막에 추가한 노드를 제거해 다른 경로를 찾는다. 사이클이 없는 그래프이므로 방문 배열이 필요 없고, 경로를 그대로 따라가며 전부 나열할 수 있다.
"""
