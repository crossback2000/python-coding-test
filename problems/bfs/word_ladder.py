"""
문제: 단어 변환 최소 단계

길이가 같은 단어들로 이루어진 목록이 주어진다. 시작 단어를 목표 단어로 바꾸기 위해 한 번에 한 글자씩만 변경할 수 있다. 매 단계마다 변경된 단어는 반드시 목록에 존재해야 한다. 시작 단어에서 목표 단어로 변환하는 최소 단계를 구하라. 단, 목표 단어가 목록에 없다면 변환할 수 없다.

입력
첫째 줄에 시작 단어와 목표 단어가 주어진다.
둘째 줄에 단어의 개수 N(1 ≤ N ≤ 5000)이 주어지고, 다음 N개의 줄에 단어가 하나씩 주어진다.

출력
시작 단어에서 목표 단어로 변환하는 최소 단계를 출력한다. 변환이 불가능하면 0을 출력한다.

예제 입력 1
hit cog
6
hot
dot
dog
lot
log
cog

예제 출력 1
5

해설 요약
한 글자씩 다른 단어끼리 간선을 두고 BFS로 탐색하면 가장 먼저 목표 단어를 방문할 때의 단계 수가 답이다.
"""

from collections import deque
from typing import Deque, Iterable, Set


def word_ladder_length(begin: str, end: str, word_list: Iterable[str]) -> int:
    """시작 단어를 목표 단어로 바꾸는 최소 단계를 반환한다."""
    words: Set[str] = set(word_list)

    # 목표 단어가 목록에 없다면 변환이 불가능하다.
    if end not in words:
        return 0

    # 아직 방문하지 않은 단어를 큐에 넣고 BFS를 시작한다.
    queue: Deque[tuple[str, int]] = deque([(begin, 1)])
    visited: Set[str] = {begin}

    while queue:
        current_word, steps = queue.popleft()

        if current_word == end:
            return steps

        # 현재 단어에서 한 글자씩 바꾸어 볼 수 있는 모든 단어를 생성한다.
        for i in range(len(current_word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == current_word[i]:
                    continue

                next_word = current_word[:i] + ch + current_word[i + 1 :]

                if next_word in words and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0


DETAILED_EXPLANATION = """
단어 변환 문제는 각 단어를 노드로 보고, 한 글자만 다른 단어끼리 간선을 잇는 그래프를 떠올리면 풀 수 있다. 간선 비용이 모두 1이므로 BFS를 사용하면 가장 적은 단계로 목표 단어에 도달할 수 있다. 현재 단어에서 한 글자씩 바꾸어 가능한 모든 다음 단어를 생성하고, 아직 방문하지 않았다면 큐에 넣는다. 목표 단어를 처음 만났을 때의 단계 수가 곧 정답이다. 이렇게 그래프 모델을 세우고 너비 우선 탐색을 적용하는 사고 과정이 핵심이다.
"""



def solve() -> None:
    """단어 변환 문제 입력을 받아 최소 단계를 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    begin, end = first_line.split()
    count_line = input().strip()
    while count_line == "":
        count_line = input().strip()
    n = int(count_line)
    words = []
    for _ in range(n):
        word = input().strip()
        while word == "":
            word = input().strip()
        words.append(word)

    print(word_ladder_length(begin, end, words))


if __name__ == "__main__":
    solve()
