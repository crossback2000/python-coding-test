"""
문제: 무방향 그래프에서 최단 이동 횟수

0번 정점에서 시작하여 무방향 그래프의 모든 정점까지의 최단 이동 횟수를 구하여라. 간선의 가중치는 모두 1이다.

입력
첫째 줄에 정점 수 N(1 ≤ N ≤ 10,000)과 간선 수 M(0 ≤ M ≤ 200,000)이 주어진다.
둘째 줄부터 M개의 줄에 걸쳐 간선을 이루는 두 정점 u, v가 주어진다. 정점 번호는 0부터 N-1까지다.

출력
정점 0에서 각 정점까지 최단 이동 횟수를 공백으로 출력한다. 도달할 수 없는 정점은 -1을 출력한다.

예제 입력 1
4 4
0 1
0 2
1 3
2 3

예제 출력 1
0 1 1 2

해설 요약
모든 간선 비용이 같으므로, 정점 0을 시작점으로 BFS를 수행하면 탐색 중 기록한 깊이가 곧 최단 이동 횟수다.
"""

from collections import deque
from typing import Deque, Dict, List

Graph = Dict[int, List[int]]


def shortest_steps_from_start(graph: Graph, start: int = 0) -> Dict[int, int]:
    """정점 start에서 각 정점까지의 최소 이동 횟수를 계산한다."""
    visited: Dict[int, int] = {start: 0}
    queue: Deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        current_distance = visited[node]

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = current_distance + 1
                queue.append(neighbor)

    return visited


DETAILED_EXPLANATION = """
그래프에서 모든 간선의 비용이 동일할 때는 BFS가 최단 경로를 찾는 가장 단순한 방법이다. 정점 0에서 시작해 큐에 넣고, 방문하지 않은 이웃을 만나면 현재 거리 + 1로 기록한다. 큐에서 꺼낸 순서가 곧 거리 순서이므로, 방문 시점에 이미 최단 거리가 확정된다. 이처럼 간선 비용이 동일한 그래프는 BFS로 해결할 수 있다는 사실을 기억하면 다양한 문제에 응용할 수 있다.
"""
