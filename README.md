# 파이썬 코딩 테스트 연습

기초 입출력 10문제, 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS) 기본기 20문제, 그리고 다양한 알고리즘을 섞은 확장 10문제까지 총 40개를 제공합니다. 각 파일에는 문제 설명과 파이썬 해설 코드가 함께 수록되어 있어 풀이 아이디어를 바로 확인할 수 있습니다.

## 디렉터리 구조
- `problems/`: 모든 문제 파일이 한 디렉터리에 모여 있습니다. 숫자로 시작하는 파일명을 직접 import하기 어려우므로, 이전과 동일한 인터페이스를 제공하는 로더 모듈(`problems/bfs.py`, `problems/dfs.py`)을 함께 제공합니다.
- `tests/`: 기존 DFS·BFS 풀이를 검증하는 `pytest` 테스트 코드

모든 문제 파일은 `solve()` 함수와 `if __name__ == "__main__":` 가드를 포함해 단일 파일로 바로 실행할 수 있게 정비했습니다. 아래와 같이 원하는 문제를 직접 실행하며 입출력을 확인할 수 있습니다.

```bash
python problems/01_tree_min_depth.py < input.txt
```

## 준비 사항
1. 별도의 패키지 의존성 없이 파이썬 3.10 이상 환경에서 실행할 수 있습니다.
2. 전체 풀이가 정상 동작하는지 확인하려면 아래 명령으로 테스트를 실행하세요.

```bash
pytest
```

문제를 먼저 직접 해결해본 후, 같은 파일에 정리된 해설과 코드를 비교하며 학습 효율을 높여보세요.

## 추천 풀이 순서 (쉬운 문제 → 어려운 문제)
1. `problems/00a_sum_two_numbers.py` — 입출력과 덧셈 익히기
2. `problems/00b_max_of_three.py` — 세 수 중 최댓값 찾기
3. `problems/00c_count_even_numbers.py` — 수열에서 짝수 세기
4. `problems/00d_min_abs_difference.py` — 인접 원소 최소 차이
5. `problems/00e_reverse_string.py` — 문자열 뒤집기
6. `problems/00f_palindrome_check.py` — 팰린드롬 판별
7. `problems/00g_count_vowels.py` — 모음 개수 세기
8. `problems/00h_running_total.py` — 누적 합 계산하기
9. `problems/00i_find_target_index.py` — 원하는 값의 첫 위치 찾기
10. `problems/00j_unique_elements.py` — 중복 제거하기
11. `problems/01_tree_min_depth.py` — 이진 트리의 최소 깊이
12. `problems/02_level_order.py` — 이진 트리 레벨 순회
13. `problems/03_combinations.py` — 조합 생성하기
14. `problems/04_permutations.py` — 순열 생성하기
15. `problems/05_target_sum.py` — 타겟 합 경우의 수
16. `problems/06_graph_shortest_steps.py` — 그래프 최단 이동 횟수
17. `problems/07_tree_path_sums.py` — 루트-리프 경로 합
18. `problems/08_island_count.py` — 섬의 개수 세기
19. `problems/09_max_region.py` — 최대 영역 넓이
20. `problems/10_spread_time.py` — 메시지 전파 시간
21. `problems/11_matrix_distance.py` — 가장 가까운 0까지 거리
22. `problems/12_rotting_oranges.py` — 오렌지 썩는 시간
23. `problems/13_maze_shortest_path.py` — 미로 최단 거리
24. `problems/14_knight_moves.py` — 나이트 최소 이동
25. `problems/15_all_paths.py` — DAG의 모든 경로
26. `problems/16_maze_paths.py` — 미로 경로의 수
27. `problems/17_word_search.py` — 격자에서 단어 찾기
28. `problems/18_open_lock.py` — 자물쇠 최소 회전 횟수
29. `problems/19_restore_ip.py` — 문자열에서 가능한 IP 주소 복원하기
30. `problems/20_word_ladder.py` — 단어 사다리 최단 단계
31. `problems/21_longest_bounded_sum.py` — 부분합이 제한된 가장 긴 구간 (슬라이딩 윈도우)
32. `problems/22_prefix_sum_queries.py` — 2차원 구간합 질의 (누적합)
33. `problems/23_classroom_scheduler.py` — 강의실 최소 개수 2 (우선순위 큐)
34. `problems/24_min_palindrome_cut.py` — 최소 회문 분할 (DP)
35. `problems/25_robot_collect_items.py` — 로봇의 체크포인트 수거 (BFS + 비트마스크 DP)
36. `problems/26_fenwick_dynamic_range_sum.py` — 실시간 구간 합 질의 (펜윅 트리)
37. `problems/27_longest_path_dag.py` — DAG에서 가장 긴 경로 (위상 정렬)
38. `problems/28_kth_shortest_path.py` — K번째 최단 경로 (다익스트라 확장)
39. `problems/29_partition_min_cost.py` — 배열 분할 최소 비용 (구간 DP)
40. `problems/30_insecticide_double_spray.py` — 살충제 2회 살포 (시뮬레이션·누적합·비트마스크)
