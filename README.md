# 파이썬 코딩 테스트 연습

깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS)에 집중한 20개의 대표 문제를 한글 해설과 함께 제공합니다. 각 파일에는 문제 설명과 파이썬 풀이가 함께 포함되어 있어 알고리즘 아이디어를 바로 확인할 수 있습니다.

## 디렉터리 구조
- `problems/dfs/`: DFS 핵심 패턴 10문제와 파이썬 해법
- `problems/bfs/`: BFS 핵심 패턴 10문제와 파이썬 해법
- `tests/`: 각 문제 풀이의 동작을 검증하는 `pytest` 테스트 코드

## 준비 사항
1. 별도의 패키지 의존성 없이 파이썬 3.10 이상 환경에서 실행할 수 있습니다.
2. 전체 풀이가 정상 동작하는지 확인하려면 아래 명령으로 테스트를 실행하세요.

```bash
pytest
```

문제를 먼저 직접 해결해본 후, 같은 파일에 정리된 해설과 코드를 비교하며 학습 효율을 높여보세요.

## 추천 풀이 순서 (쉬운 문제 → 어려운 문제)
1. `problems/bfs/01_tree_min_depth.py` — 이진 트리의 최소 깊이
2. `problems/bfs/02_level_order.py` — 이진 트리 레벨 순회
3. `problems/dfs/03_combinations.py` — 조합 생성하기
4. `problems/dfs/04_permutations.py` — 순열 생성하기
5. `problems/dfs/05_target_sum.py` — 타겟 합 경우의 수
6. `problems/bfs/06_graph_shortest_steps.py` — 그래프 최단 이동 횟수
7. `problems/dfs/07_tree_path_sums.py` — 루트-리프 경로 합
8. `problems/dfs/08_island_count.py` — 섬의 개수 세기
9. `problems/dfs/09_max_region.py` — 최대 영역 넓이
10. `problems/bfs/10_spread_time.py` — 메시지 전파 시간
11. `problems/bfs/11_matrix_distance.py` — 가장 가까운 0까지 거리
12. `problems/bfs/12_rotting_oranges.py` — 오렌지 썩는 시간
13. `problems/bfs/13_maze_shortest_path.py` — 미로 최단 거리
14. `problems/bfs/14_knight_moves.py` — 나이트 최소 이동
15. `problems/dfs/15_all_paths.py` — DAG의 모든 경로
16. `problems/dfs/16_maze_paths.py` — 미로 경로의 수
17. `problems/dfs/17_word_search.py` — 단어 찾기
18. `problems/bfs/18_open_lock.py` — 자물쇠 최소 회전 횟수
19. `problems/dfs/19_restore_ip.py` — IP 주소 복원
20. `problems/bfs/20_word_ladder.py` — 단어 사다리 최단 단계
