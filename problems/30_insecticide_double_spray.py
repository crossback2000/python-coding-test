"""
문제: 살충제 2회 살포 (시뮬레이션 + 2D 누적합 + 비트마스크)

N×N 격자에 K마리의 벌레가 있다. 각 벌레는 위치 (r, c), 이동 방향 d(1: 동, 2: 서, 3: 남, 4: 북),
속도 s를 가진다. 모든 벌레는 매 초마다 자신의 방향으로 s칸 이동하며, 격자 경계를 만나면
즉시 반사되어 방향을 반대로 바꾼 뒤 남은 거리를 이동한다. 같은 칸에 여러 벌레가 있을 수 있다.

살충제는 한 번에 M×M 크기의 정사각형 범위에만 뿌릴 수 있으며, 최대 두 번 사용할 수 있다.
살포 시점과 위치는 자유롭게 선택할 수 있고, 살포된 순간 범위 안의 모든 벌레는 즉시 사라진다.
두 번의 살포로 제거할 수 있는 벌레의 최대 수를 구하라.

입력
첫째 줄에 테스트 케이스 수 T(1 ≤ T ≤ 10)가 주어진다.
각 테스트 케이스마다 다음 형식으로 입력이 주어진다.
- N M K
- 이후 K개의 줄에 r c d s 가 주어진다. (1 ≤ r, c ≤ N, 1 ≤ s ≤ 1000)

출력
각 테스트 케이스마다 최대 제거 가능한 벌레 수를 한 줄에 하나씩 출력한다.

해설 요약
한 축의 움직임은 주기 cycle = 2×(N−1)을 갖는다. 시간 t에서의 위치는 초기 위치와
"방향 × (s × t mod cycle)" 만큼 이동한 결과를 반사 규칙으로 접어 계산할 수 있다.
주기가 cycle이므로 t = 0..cycle−1 구간만 조사해도 모든 상황을 포함한다.
각 시각별로 격자에 벌레 수를 세어 2차원 누적합으로 모든 M×M 구간의 벌레 수를 구하고,
상위 몇 개 구역만 후보로 뽑아 해당 구역에 포함되는 벌레 집합을 비트마스크로 저장한다.
이후 후보 쌍의 합집합 크기를 계산해 두 번의 살포로 제거할 수 있는 최대 수를 찾는다.
"""

from typing import List, Optional, Tuple

# 방향을 행/열 증가량으로 매핑한다. 동/서/남/북 순서.
DIRECTION = {
    1: (0, 1),   # 동 -> 열 증가
    2: (0, -1),  # 서 -> 열 감소
    3: (1, 0),   # 남 -> 행 증가
    4: (-1, 0),  # 북 -> 행 감소
}


class Bug:
    """벌레의 초기 상태를 보관하는 자료구조."""

    def __init__(self, row: int, col: int, direction: int, speed: int) -> None:
        # 입력이 1-indexed이므로 계산 편의를 위해 0-indexed로 보관한다.
        self.row = row - 1
        self.col = col - 1
        self.direction = direction
        self.speed = speed

    def position_at(self, time: int, size: int) -> Tuple[int, int]:
        """주기성을 이용해 time 초 뒤 위치를 계산한다."""

        cycle = 2 * (size - 1)
        dr, dc = DIRECTION[self.direction]
        move = (self.speed * time) % cycle

        def advance(coord: int, delta: int) -> int:
            # delta는 +1/-1 중 하나로, 이동 방향을 나타낸다.
            raw = (coord + delta * move) % cycle
            # 경계를 넘어서면 반사되므로, cycle보다 크면 접어준다.
            return raw if raw < size else cycle - raw

        new_row = advance(self.row, dr)
        new_col = advance(self.col, dc)
        return new_row, new_col


class Candidate:
    """한 시각의 특정 살포 위치 정보를 담는다."""

    def __init__(self, count: int, row: int, col: int, mask: int) -> None:
        self.count = count
        self.row = row
        self.col = col
        self.mask = mask


def gather_candidates(
    bugs: List[Bug],
    size: int,
    square: int,
    top_k: Optional[int] = None,
) -> List[Candidate]:
    """모든 시각에 대해 상위 구간 후보를 모아 반환한다."""

    cycle = 2 * (size - 1)
    candidates: List[Candidate] = []

    for t in range(cycle):
        # 1) 모든 벌레의 위치를 계산하고 격자에 개수를 적재한다.
        counts = [[0] * size for _ in range(size)]
        positions: List[Tuple[int, int, int]] = []  # (r, c, bug_id)
        for bug_id, bug in enumerate(bugs):
            r, c = bug.position_at(t, size)
            counts[r][c] += 1
            positions.append((r, c, bug_id))

        # 2) 2D 누적합을 만들어 모든 M×M 구역의 벌레 수를 O(1)에 얻는다.
        prefix = [[0] * (size + 1) for _ in range(size + 1)]
        for r in range(1, size + 1):
            row_sum = 0
            for c in range(1, size + 1):
                row_sum += counts[r - 1][c - 1]
                prefix[r][c] = prefix[r - 1][c] + row_sum

        def area_sum(r: int, c: int) -> int:
            # 좌상단 (r, c)에서 시작하는 square×square 영역의 총 벌레 수
            r2, c2 = r + square, c + square
            return (
                prefix[r2][c2]
                - prefix[r][c2]
                - prefix[r2][c]
                + prefix[r][c]
            )

        # 3) 가장 많은 벌레가 모인 구역을 고른다.
        best: List[Tuple[int, int, int]] = []  # (count, r, c)
        limit = size - square + 1
        if top_k is None:
            # 정밀 탐색: 모든 구역을 후보로 포함한다.
            for r in range(limit):
                for c in range(limit):
                    cnt = area_sum(r, c)
                    best.append((cnt, r, c))
        else:
            # 후보 수를 제한해 탐색 공간을 줄인다.
            for r in range(limit):
                for c in range(limit):
                    cnt = area_sum(r, c)
                    if len(best) < top_k:
                        best.append((cnt, r, c))
                        best.sort(reverse=True)
                    elif cnt > best[-1][0]:
                        best[-1] = (cnt, r, c)
                        best.sort(reverse=True)

        # 4) 각 후보 구역에 포함되는 벌레 id를 비트마스크로 만든다.
        for cnt, r, c in best:
            mask = 0
            if cnt > 0:
                for pr, pc, bug_id in positions:
                    if r <= pr < r + square and c <= pc < c + square:
                        mask |= 1 << bug_id
            candidates.append(Candidate(cnt, r, c, mask))

    return candidates


def max_kills_with_two_sprays(n: int, m: int, bugs: List[Bug]) -> int:
    """모든 후보 구간을 탐색해 두 번의 살포로 제거 가능한 최대 벌레 수를 계산한다."""

    candidates = gather_candidates(bugs, n, m)

    max_kill = 0
    total = len(candidates)
    for i in range(total):
        for j in range(i, total):
            union_mask = candidates[i].mask | candidates[j].mask
            kill_count = union_mask.bit_count()
            if kill_count > max_kill:
                max_kill = kill_count
    return max_kill


DETAILED_EXPLANATION = """
반사 이동은 한 축당 2×(N−1) 길이의 주기를 갖는다. 따라서 모든 벌레의 위치는 t=0..cycle−1 내에서 반복된다.
이 사실을 이용해 매 시각 벌레 위치를 계산하고, 2차원 누적합으로 모든 M×M 영역의 벌레 수를 얻는다.
모든 영역을 다 저장하면 조합 수가 크므로, 각 시각마다 가장 벌레가 많은 상위 몇 개 후보만 남긴다.
후보마다 어떤 벌레가 포함되는지 비트마스크(mask)로 기록해 두면, 두 후보의 합집합 크기는
(mask1 | mask2).bit_count() 로 O(1)에 계산된다. 모든 후보 쌍을 탐색해 최댓값을 구한다.
"""


def solve() -> None:
    """입력을 받아 두 번의 살포로 제거 가능한 최대 벌레 수를 출력한다."""

    import sys

    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return

    t = int(line)
    outputs = []
    for _ in range(t):
        n, m, k = map(int, input().split())
        bugs = []
        for _ in range(k):
            r, c, d, s = map(int, input().split())
            bugs.append(Bug(r, c, d, s))

        outputs.append(str(max_kills_with_two_sprays(n, m, bugs)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
