# https://leetcode.com/problems/number-of-islands/description

from typing import List
from collections import deque

# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            grid[i][j] = '0'
            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= r < m and 0 <= c < n):
                    continue
                
                if grid[r][c] == '1':
                    dfs(r,c)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans = ans + 1
                    dfs(i,j)
        
        return ans
        