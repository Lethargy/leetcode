# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

from typing import List

# DP + DFS
from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        @cache
        def v(i,j):
            out = 1
            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= r < n and 0 <= c < m and matrix[r][c] > matrix[i][j]:
                    out = max(out, 1 + v(r,c))

            return out

        return max(v(i,j) for i in range(n) for j in range(m))

# BFS
from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        L = [[1] * m for _ in range(n)]
        q = deque([])

        for i in range(n):
            for j in range(m):
                for (r,c) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if not (0 <= r < n and 0 <= c < m):
                        continue
                    
                    if matrix[i][j] < matrix[r][c]:
                        L[i][j] = 0
                        break

                if L[i][j] == 1:
                    q.append((i,j))

        while q:
            i,j = q.popleft()
            for (r,c) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if not (0 <= r < n and 0 <= c < m):
                    continue

                if matrix[r][c] < matrix[i][j]:
                    if L[i][j] + 1 > L[r][c]:
                        L[r][c] = L[i][j] + 1
                        q.append((r,c))

        return max(max(r) for r in L)