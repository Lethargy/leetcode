# https://leetcode.com/problems/number-of-closed-islands

from typing import List
from collections import deque

# BFS

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def bfs(i,j): # change grid[i][j] from 0 to 1, and its neighbors likewise
            q = deque([(i,j)])
            while q:
                r0,c0 = q.popleft()
                grid[r0][c0] = 1
                for r1, c1 in [(r0+1,c0), (r0-1,c0), (r0,c0+1), (r0,c0-1)]:
                    if not (0 <= r1 < n and 0 <= c1 < m):
                        continue
                    if grid[r1][c1] == 0:
                        q.append((r1,c1))
        
        # first, take care of boundary
        for i in range(n):
            if grid[i][0] == 0:
                bfs(i,0)
            if grid[i][m-1] == 0:
                bfs(i,m-1)
        
        for j in range(m):
            if grid[0][j] == 0:
                bfs(0,j)
            if grid[n-1][j] == 0:
                bfs(n-1,j)

        ans = 0

        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j] == 0:
                    ans = ans + 1
                    bfs(i,j)

        return ans
    
# DFS

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):
            grid[i][j] = 1
            for r, c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= r < n and 0 <= c < m):
                    continue
                
                if grid[r][c] == 0:
                    dfs(r,c)
        
        for i in range(n):
            if grid[i][0] == 0:
                dfs(i,0)
            if grid[i][m-1] == 0:
                dfs(i,m-1)
        
        for j in range(m):
            if grid[0][j] == 0:
                dfs(0,j)
            if grid[n-1][j] == 0:
                dfs(n-1,j)

        ans = 0

        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j] == 0:
                    ans = ans + 1
                    dfs(i,j)

        return ans

