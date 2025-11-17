# 실행: python 20.py < input.txt
"""
문제: 네트워크 메시지 전파 시간

무방향 그래프 형태의 네트워크에서 한 노드에서 시작한 메시지가 모든 노드로 전파되는 데 걸리는 최소 시간을 구하여라. 간선 하나를 타는 데는 1단위 시간이 걸린다. 모든 노드가 메시지를 받을 수 없다면 -1을 출력한다.

입력
첫째 줄에 노드 수 N(1 ≤ N ≤ 10,000)과 간선 수 M(0 ≤ M ≤ 200,000)이 주어진다.
둘째 줄부터 M개의 줄에 간선으로 연결된 두 노드 u, v가 주어진다.
마지막 줄에 메시지를 보낸 시작 노드 s가 주어진다.

출력
모든 노드가 메시지를 받는 데 걸리는 최소 시간을 출력하라. 연결되지 않은 노드가 있다면 -1을 출력한다.

예제 입력 1
4 3
0 1
1 2
2 3
0

예제 출력 1
3

해설 요약
시작 노드에서 BFS를 실행해 각 노드까지의 거리를 구하면, 가장 먼 노드까지의 거리(깊이)가 전파 완료 시간이다.
"""

from collections import deque
from typing import Deque, Dict, List

Graph = Dict[int, List[int]]


def spread_time(graph: Graph, start: int) -> int:
    """시작 노드에서 전체 네트워크로 메시지가 퍼지는 데 걸리는 시간을 구한다."""
    visited: Dict[int, int] = {start: 0}
    queue: Deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        current_time = visited[node]

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = current_time + 1
                queue.append(neighbor)

    # 그래프에 존재하는 노드가 모두 visited에 기록되었는지 확인한다.
    if len(visited) != len(graph):
        return -1

    return max(visited.values())


DETAILED_EXPLANATION = """
메시지를 전파하는 상황은 그래프에서 최단 거리를 구하는 문제로 바꿀 수 있다. 시작 노드에서 BFS를 돌리면 각 노드에 도달하는 최소 시간이 계산된다. 모든 노드가 방문되었다면 그중 가장 큰 값이 전체 전파에 걸린 시간이 된다. 만약 방문하지 못한 노드가 있다면 연결되지 않은 노드가 있다는 뜻이므로 -1을 반환한다. BFS를 이용한 거리 계산 패턴을 네트워크 문제에 적용한 예시다.
"""



def solve() -> None:
    """그래프 입력을 받아 메시지 전파 시간을 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, m = map(int, first_line.split())
    graph: Graph = {i: [] for i in range(n)}
    for _ in range(m):
        line = input().strip()
        while line == "":
            line = input().strip()
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)

    start_line = input().strip()
    while start_line == "":
        start_line = input().strip()
    start = int(start_line)

    print(spread_time(graph, start))


if __name__ == "__main__":
    solve()
