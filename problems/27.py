# 실행: python 27.py < input.txt
"""
문제
단어 찾기
- 대문자 알파벳으로 이루어진 N×M 보드와 찾고자 하는 단어가 주어진다. 한 칸에서 시작해 상하좌우로 인접한 칸을 한 번씩만 사용하며 문자를 이어 붙였을 때 주어진 단어를 만들 수 있는지 판별하라.

입력
첫째 줄에 N과 M(1 ≤ N, M ≤ 6)이 주어진다.
둘째 줄부터 N개의 줄에 각 줄마다 길이 M의 대문자 문자열이 주어진다.
마지막 줄에 찾고자 하는 단어가 주어진다.

출력
단어를 만들 수 있으면 YES, 아니면 NO를 출력한다.

제한
1 ≤ N, M ≤ 6

예제
입력
3 4
ABCE
SFCS
ADEE
ABCCED

출력
YES

해설
각 칸을 시작점으로 DFS를 수행하며, 방문한 칸을 임시로 표시해 중복 사용을 막으면 된다.

"""

from typing import Iterable, List


def exist_word(board: Iterable[Iterable[str]], word: str) -> bool:
    """DFS 백트래킹으로 단어를 만들 수 있는지 확인한다."""
    grid: List[List[str]] = [list(row) for row in board]
    if not grid:
        return False

    n_rows = len(grid)
    n_cols = len(grid[0])
    word_length = len(word)

    def dfs(r: int, c: int, index: int) -> bool:
        # 모든 글자를 찾았다면 성공이다.
        if index == word_length:
            return True

        if not (0 <= r < n_rows and 0 <= c < n_cols):
            return False
        if grid[r][c] != word[index]:
            return False

        # 현재 칸을 방문 처리하여 다시 사용되지 않도록 한다.
        temp = grid[r][c]
        grid[r][c] = "#"

        # 상하좌우 네 방향으로 이동해 나머지 글자를 찾는다.
        if (
            dfs(r + 1, c, index + 1)
            or dfs(r - 1, c, index + 1)
            or dfs(r, c + 1, index + 1)
            or dfs(r, c - 1, index + 1)
        ):
            grid[r][c] = temp
            return True

        # 탐색이 실패하면 방문 표시를 되돌린다.
        grid[r][c] = temp
        return False

    for row in range(n_rows):
        for col in range(n_cols):
            if dfs(row, col, 0):
                return True

    return False


DETAILED_EXPLANATION = """
단어 찾기 문제는 DFS 백트래킹의 대표적인 예시다. 각 칸을 시작점으로 삼고, 단어의 첫 글자가 일치하면 인접한 칸으로 이동하며 다음 글자를 찾는다. 한 경로에서 같은 칸을 두 번 사용할 수 없으므로, 방문한 칸을 임시로 다른 문자로 바꿔 중복 사용을 막는다. 만약 끝까지 도달하면 성공이고, 실패하면 방문 표시를 되돌린다. 이렇게 경로를 하나씩 시도하며 정답을 찾는 과정을 통해 DFS 백트래킹의 흐름을 이해할 수 있다.
"""



def solve() -> None:
    """보드와 단어를 입력받아 존재 여부를 출력한다."""

    import sys

    input = sys.stdin.readline

    first_line = input().strip()
    if not first_line:
        return

    n, m = map(int, first_line.split())
    board = []
    for _ in range(n):
        line = input().strip()
        while line == "":
            line = input().strip()
        board.append(list(line))

    word = input().strip()
    while word == "":
        word = input().strip()

    result = exist_word(board, word)
    print("YES" if result else "NO")


if __name__ == "__main__":
    solve()
