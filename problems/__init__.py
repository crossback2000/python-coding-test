"""코딩 테스트 문제 모음 패키지.

DFS/BFS 문제를 비롯해 다양한 주제를 하나의 디렉터리에 모아두고,
숫자로 시작하는 파일을 importlib로 불러오는 헬퍼 모듈(bfs.py, dfs.py)을 제공한다.
"""
from __future__ import annotations

from . import bfs, dfs

__all__ = ["bfs", "dfs"]
