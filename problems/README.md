# DFS·BFS 및 종합 알고리즘 문제 모음

하나의 디렉터리에 총 40개의 파이썬 풀이 예제가 담겨 있습니다. 숫자로 시작하는 파일을 편하게 불러오도록 `problems/bfs.py`와 `problems/dfs.py` 로더 모듈을 제공하며, 각 문제 파일에는 한글 설명과 함께 동작하는 해설 코드가 포함되어 있습니다.

모든 문제는 `solve()` 함수와 `__main__` 가드를 갖추고 있어 다음과 같이 단일 파일로 바로 실행할 수 있습니다.

```bash
python problems/14_knight_moves.py < input.txt
```

## 입문 문제 (기본 입출력 & 자료구조 패턴)
1. `00a_sum_two_numbers.py`: 두 수의 합 구하기
2. `00b_max_of_three.py`: 세 수 중 최댓값 찾기
3. `00c_count_even_numbers.py`: 수열에서 짝수 개수 세기
4. `00d_min_abs_difference.py`: 인접 원소 최소 차이
5. `00e_reverse_string.py`: 문자열 뒤집기
6. `00f_palindrome_check.py`: 팰린드롬 여부 판별
7. `00g_count_vowels.py`: 문자열에서 모음 개수 세기
8. `00h_running_total.py`: 누적 합 배열 만들기
9. `00i_find_target_index.py`: 원하는 값의 첫 위치 찾기
10. `00j_unique_elements.py`: 등장 순서를 유지한 중복 제거

## DFS 문제 목록 (난이도 순)
1. `03_combinations.py`: 조합 생성하기
2. `04_permutations.py`: 숫자 목록의 모든 순열 생성
3. `05_target_sum.py`: 부호 조합으로 목표 합 만들기
4. `07_tree_path_sums.py`: 이진트리 루트-리프 경로 합 구하기
5. `08_island_count.py`: 2차원 격자에서 섬의 개수 세기
6. `09_max_region.py`: 가장 큰 연결 영역 넓이 계산
7. `15_all_paths.py`: DAG에서 모든 경로 나열하기
8. `16_maze_paths.py`: 미로 경로 수 세기
9. `17_word_search.py`: 격자에서 단어 찾기
10. `19_restore_ip.py`: 문자열에서 가능한 IP 주소 복원하기

## BFS 문제 목록 (난이도 순)
1. `01_tree_min_depth.py`: 이진트리 최소 깊이 찾기
2. `02_level_order.py`: 이진트리 레벨 순회 결과 구하기
3. `06_graph_shortest_steps.py`: 그래프 최단 이동 횟수
4. `10_spread_time.py`: 그래프 확산 완료 시간 측정
5. `11_matrix_distance.py`: 0에 대한 최소 거리 행렬
6. `12_rotting_oranges.py`: 오렌지 썩는 시간 계산
7. `13_maze_shortest_path.py`: 미로 최단 거리 구하기
8. `14_knight_moves.py`: 체스판 나이트 최소 이동
9. `18_open_lock.py`: 자물쇠 최소 회전 수 계산
10. `20_word_ladder.py`: 단어 사다리 최단 단계

## 확장 알고리즘 문제 목록 (난이도 순)
1. `21_longest_bounded_sum.py`: 부분합이 제한된 가장 긴 구간 (슬라이딩 윈도우)
2. `22_prefix_sum_queries.py`: 2차원 구간합 질의 (누적합)
3. `23_classroom_scheduler.py`: 강의실 최소 개수 2 (우선순위 큐)
4. `24_min_palindrome_cut.py`: 최소 회문 분할 (구간 DP)
5. `25_robot_collect_items.py`: 로봇의 체크포인트 수거 (BFS + 비트마스크 DP)
6. `26_fenwick_dynamic_range_sum.py`: 실시간 구간 합 질의 (펜윅 트리)
7. `27_longest_path_dag.py`: DAG에서 가장 긴 경로 (위상 정렬)
8. `28_kth_shortest_path.py`: K번째 최단 경로 (다익스트라 확장)
9. `29_partition_min_cost.py`: 배열 분할 최소 비용 (구간 DP)
10. `30_insecticide_double_spray.py`: 살충제 2회 살포 (시뮬레이션·누적합·비트마스크)

각 문제는 README와 동일한 추천 순서로 나열되어 있으며, `tests/test_problems.py`는 기존 DFS/BFS 풀이를 검증합니다. 새로 추가된 문제들은 바로 실행하여 입출력을 확인할 수 있도록 `solve()` 함수를 포함하고 있습니다.
