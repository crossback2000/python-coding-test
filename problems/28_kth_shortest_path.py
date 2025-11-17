"""
문제: K번째 최단 경로 (우선순위 큐 확장 다익스트라)

가중치가 양수인 방향 그래프가 주어진다. 시작점에서 모든 노드까지의 "K번째 최단 경로"
길이를 구하라. K번째 경로가 존재하지 않는다면 -1을 출력한다.

입력
첫째 줄에 정점 수 N(1 ≤ N ≤ 2,000), 간선 수 M(0 ≤ M ≤ 50,000), 그리고 K(1 ≤ K ≤ 100)가 주어진다.
이후 M개의 줄에 u v w 형태로 간선이 주어진다. 이는 u에서 v로 가중치 w의 간선이 있음을 의미한다.
마지막 줄에 시작 정점 S가 주어진다. 모든 가중치는 1 이상 10,000 이하이다.

출력
각 정점에 대해 S에서 해당 정점까지의 K번째 최단 경로 길이를 한 줄에 하나씩 1번 정점부터 출력한다.
경로가 K개 미만이면 -1을 출력한다.

해설 요약
기존 다익스트라는 한 노드당 최단 거리 하나만 관리하지만, 여기서는 최대 K개까지 거리를 저장한다.
우선순위 큐에서 거리를 꺼낼 때마다 해당 노드의 리스트에 추가하고, 아직 K개 미만일 때만 간선을 확장한다.
이렇게 하면 각 노드에서 최대 K번만 확장되므로 전체 시간은 O(K * M log (K*N)) 수준으로 동작한다.
"""

import heapq
from typing import List, Tuple


def kth_shortest_paths(n: int, edges: List[Tuple[int, int, int]], start: int, k: int) -> List[int]:
    """모든 정점까지의 K번째 최단 경로 길이를 구한다."""

    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))

    # 각 노드별로 발견된 경로 길이를 저장 (오름차순 유지)
    dist_list: List[List[int]] = [[] for _ in range(n + 1)]

    # (거리, 노드)를 담는 우선순위 큐. 시작점에서 거리 0으로 시작한다.
    pq: List[Tuple[int, int]] = [(0, start)]

    while pq:
        cur_dist, node = heapq.heappop(pq)

        # 이미 k개의 경로를 찾았다면 더 이상 처리하지 않는다.
        if len(dist_list[node]) >= k:
            continue

        # 현재 거리를 리스트에 저장한다.
        dist_list[node].append(cur_dist)

        # 노드가 k번 미만으로 팝된 경우, 현재 경로를 기반으로 이웃을 확장한다.
        for nxt, weight in graph[node]:
            next_dist = cur_dist + weight
            heapq.heappush(pq, (next_dist, nxt))

    # 각 노드에 대해 k번째 거리가 있으면 반환하고, 없으면 -1로 채운다.
    result = [-1] * n
    for node in range(1, n + 1):
        if len(dist_list[node]) >= k:
            result[node - 1] = dist_list[node][k - 1]
    return result


DETAILED_EXPLANATION = """
우선순위 큐에 (거리, 정점)을 넣고 팝하면서, 각 정점의 거리 리스트를 채운다. 어떤 정점이 k번 이상 큐에서 나오면 더 이상
확장하지 않으므로, 간선 확장 횟수는 각 정점당 최대 k번이다. dist_list[node]에 저장되는 거리들은 큐의 특성상 오름차순으로
채워지므로 k번째 값이 곧 k번째 최단 경로 길이이다. 다익스트라의 변형으로, 모든 가중치가 양수라는 가정이 필요하다.
"""


def solve() -> None:
    """입력을 받아 모든 정점의 K번째 최단 경로 길이를 출력한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    n, m, k = map(int, line.split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    start = int(input())

    results = kth_shortest_paths(n, edges, start, k)
    sys.stdout.write("\n".join(map(str, results)))


if __name__ == "__main__":
    solve()
