# https://leetcode.com/problems/max-area-of-island

from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j,a):
            grid[i][j] = 0
            a = a + 1

            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= r < m and 0 <= c < n):
                    continue
                
                if grid[r][c] == 1:
                    a = dfs(r,c,a)
                
            return a

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j,0))
        
        return ans
