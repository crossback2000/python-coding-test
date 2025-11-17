# 실행: python 30.py < input.txt
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

from collections import defaultdict, deque
from typing import Deque, Dict, Iterable, List, Set


def word_ladder_length(begin: str, end: str, word_list: Iterable[str]) -> int:
    """시작 단어를 목표 단어로 바꾸는 최소 단계를 반환한다."""

    # 목록에 있는 단어는 중복 없이 관리한다.
    words: Set[str] = set(word_list)
    if end not in words:
        return 0

    # 한 글자만 다른 단어를 빠르게 찾기 위해 패턴별로 단어를 묶는다.
    pattern_map: Dict[str, List[str]] = defaultdict(list)
    all_words = list(words)
    all_words.append(begin)
    word_length = len(begin)

    for word in all_words:
        for i in range(word_length):
            pattern = word[:i] + "*" + word[i + 1 :]
            pattern_map[pattern].append(word)

    queue: Deque[tuple[str, int]] = deque([(begin, 1)])
    visited: Set[str] = {begin}

    while queue:
        current_word, steps = queue.popleft()
        if current_word == end:
            return steps

        for i in range(word_length):
            pattern = current_word[:i] + "*" + current_word[i + 1 :]

            for next_word in pattern_map[pattern]:
                if next_word in visited:
                    continue
                visited.add(next_word)
                queue.append((next_word, steps + 1))

            # 동일한 패턴으로 다시 접근하지 않도록 리스트를 비워 준다.
            pattern_map[pattern].clear()

    return 0


DETAILED_EXPLANATION = """
단어 변환 문제는 각 단어를 정점으로 보고, 한 글자만 다른 단어끼리 간선을 잇는 그래프로 모델링한다. 코딩 테스트에서는 패턴을 사용해
가능한 이웃 단어를 빠르게 찾는 방식이 자주 쓰인다. 각 단어에서 한 글자를 * 로 치환한 패턴을 만들고, 같은 패턴을 공유하는 단어끼리
인접 리스트처럼 묶는다. 이렇게 전처리를 해두면 BFS 과정에서 알파벳 26개를 모두 시도하지 않아도 되어 탐색 속도가 빨라진다. 시작
단어를 큐에 넣고, 패턴을 통해 한 단계에 갈 수 있는 단어들을 방문하며 목표 단어를 처음 만났을 때의 단계 수를 반환한다. 전형적인
그래프 모델링과 BFS + 패턴 전처리 조합은 백준이나 카카오 같은 코딩 테스트에서 자주 쓰이는 접근법이다.
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
