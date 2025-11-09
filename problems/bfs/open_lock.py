"""
문제: 자물쇠 비밀번호 최소 회전 횟수

네 자리 숫자 자물쇠가 있다. 각 자리 숫자는 0에서 9까지이며, 한 번의 회전에 해당 자리 숫자를 +1 또는 -1로 바꿀 수 있다. 주어진 금지 상태(Deadend)를 피하면서 시작 상태 "0000"에서 목표 상태로 이동하는 최소 회전 횟수를 구하여라. 숫자는 0에서 아래로 1을 빼면 9로, 9에서 위로 1을 더하면 0으로 순환한다.

입력
첫째 줄에 금지 상태의 개수 N(0 ≤ N ≤ 10,000)이 주어진다.
둘째 줄부터 N개의 줄에 금지 상태 네 자리 문자열이 주어진다.
마지막 줄에 목표 상태가 주어진다.

출력
최소 회전 횟수를 출력한다. 목표 상태에 도달할 수 없으면 -1을 출력한다.

예제 입력 1
5
0201
0101
0102
1212
2002
0202

예제 출력 1
6

해설 요약
자물쇠의 상태를 그래프의 정점으로 보고 BFS를 수행하면, 가장 먼저 목표 상태를 방문했을 때의 회전 횟수가 최소이다.
"""

from collections import deque
from typing import Deque, Iterable, Set


def minimum_turns_to_unlock(deadends: Iterable[str], target: str) -> int:
    """금지 상태를 피하며 목표 상태로 이동하는 최소 회전 횟수를 계산한다."""
    dead: Set[str] = set(deadends)

    start = "0000"
    if start in dead:
        return -1
    if target == start:
        return 0

    queue: Deque[tuple[str, int]] = deque([(start, 0)])
    visited: Set[str] = {start}

    while queue:
        state, turns = queue.popleft()

        for i in range(4):
            digit = int(state[i])

            for diff in (-1, 1):
                next_digit = (digit + diff) % 10
                next_state = state[:i] + str(next_digit) + state[i + 1 :]

                if next_state in dead or next_state in visited:
                    continue

                if next_state == target:
                    return turns + 1

                visited.add(next_state)
                queue.append((next_state, turns + 1))

    return -1


DETAILED_EXPLANATION = """
자물쇠의 가능한 모든 상태를 노드로 보고, 한 번의 회전으로 바뀌는 상태를 간선으로 생각하면 그래프 문제가 된다. 각 간선의 비용이 1이므로 BFS를 사용하면 최소 회전 횟수를 보장할 수 있다. 시작 상태를 큐에 넣고 한 자리씩 +1, -1을 적용하여 새 상태를 생성한다. 금지 상태나 이미 방문한 상태는 건너뛰고, 목표 상태를 처음 만났을 때의 회전 횟수를 반환한다. 그래프 모델링과 BFS 적용이라는 두 가지 아이디어가 핵심이다.
"""
