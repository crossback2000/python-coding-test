# 실행: python 37.py < input.txt
"""
문제
DAG에서 가장 긴 경로 (위상 정렬 + DP)
- 방향성이 있는 비순환 그래프(DAG)가 주어질 때, 가장 긴 경로의 길이를 구하라. 노드 수 N과 간선 수 M은 최대 200,000까지 가능하다. 경로 길이는 방문한 간선의 수로 정의한다.

입력
첫째 줄에 N(1 ≤ N ≤ 200,000)과 M(0 ≤ M ≤ 200,000)이 주어진다.
이후 M개의 줄에 u v 형식으로 간선이 주어진다. 이는 u에서 v로 가는 간선이 있음을 의미한다.

출력
DAG 상에서 가능한 가장 긴 경로의 길이를 출력한다.

제한
1 ≤ N ≤ 200,000 / 0 ≤ M ≤ 200,000

예제
입력
4 4
1 2
2 3
1 3
3 4

출력
3

해설
DAG에서는 위상 정렬 순서대로 노드를 순회하면 모든 간선이 앞으로만 향한다. 각 노드의 최장 경로 길이를 dp로 저장하며 위상 순서대로 업데이트하면 전체 최장 경로를 얻을 수 있다.

"""

from collections import deque
from typing import List


def longest_path_dag(n: int, edges: List[List[int]]) -> int:
    """위상 정렬과 DP를 이용해 DAG의 최장 경로 길이를 계산한다."""

    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u - 1].append(v - 1)
        indegree[v - 1] += 1

    # 위상 정렬 시작 노드: 진입 차수가 0인 모든 정점
    queue = deque([i for i in range(n) if indegree[i] == 0])

    # 각 노드까지의 최장 경로 길이 (간선 수 기준)
    dist = [0] * n
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1
        for nxt in graph[node]:
            # node를 거쳐 nxt로 가는 경우의 길이 후보
            if dist[node] + 1 > dist[nxt]:
                dist[nxt] = dist[node] + 1
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if processed != n:
        raise ValueError("그래프가 DAG가 아닙니다")

    return max(dist)


DETAILED_EXPLANATION = """
DAG에서는 사이클이 없으므로 위상 정렬이 가능하다. 진입 차수가 0인 노드부터 시작해 큐에 넣고, 간선을 따라가며
차수를 감소시킨다. 위상 순서대로 노드를 꺼내면서 dist[nxt] = max(dist[nxt], dist[cur] + 1) 로 갱신하면 모든 경로를
탐색한 것과 동일한 효과를 낸다. 각 노드는 한 번만 큐에서 나오므로 시간 복잡도는 O(N + M)이다.
"""


def solve() -> None:
    """입력을 받아 DAG 최장 경로 길이를 계산한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    n, m = map(int, line.split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    print(longest_path_dag(n, edges))


if __name__ == "__main__":
    solve()
