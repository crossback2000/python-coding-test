"""
문제: 가능한 IP 주소 복원하기

숫자로만 이루어진 문자열이 주어진다. 이 문자열을 네 개의 숫자 조각으로 나누어 올바른 IPv4 주소를 만들 수 있는 모든 경우를 구하여라. 각 조각은 0에서 255 사이의 정수여야 하며, 0으로 시작하는 경우는 0 자체만 허용된다.

입력
첫째 줄에 문자열이 주어진다. 문자열 길이는 4 이상 12 이하이다.

출력
가능한 모든 IP 주소를 한 줄에 하나씩 출력한다.

예제 입력 1
25525511135

예제 출력 1
255.255.11.135
255.255.111.35

해설 요약
DFS 백트래킹으로 조각의 길이를 1~3까지 시도하면서 조건을 만족하는지 검사하면 모든 경우를 찾을 수 있다.
"""

from typing import List


def restore_ip_addresses(s: str) -> List[str]:
    """DFS 백트래킹으로 가능한 모든 IP 주소를 생성한다."""
    result: List[str] = []
    parts: List[str] = []

    def is_valid(part: str) -> bool:
        if len(part) > 1 and part[0] == "0":
            return False
        if not 0 <= int(part) <= 255:
            return False
        return True

    def dfs(index: int) -> None:
        if len(parts) == 4:
            if index == len(s):
                result.append(".".join(parts))
            return

        # 조각의 길이는 1~3 사이만 가능하다.
        for length in range(1, 4):
            if index + length > len(s):
                break

            part = s[index : index + length]
            if not is_valid(part):
                continue

            parts.append(part)
            dfs(index + length)
            parts.pop()

    dfs(0)
    return result


DETAILED_EXPLANATION = """
문자열을 네 부분으로 나누는 모든 경우를 시도해야 하므로 DFS 백트래킹을 활용한다. 재귀 함수는 현재까지 만든 조각 수와 다음에 탐색할 시작 위치를 기억한다. 길이 1~3을 시도하면서 조건에 맞는 조각만 선택하고, 네 개의 조각을 만들었을 때 문자열을 모두 사용했다면 정답 리스트에 추가한다. 선택을 되돌리며 모든 가능성을 탐색하는 전형적인 백트래킹 접근법이다.
"""
