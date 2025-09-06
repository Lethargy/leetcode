# https://leetcode.com/problems/minimum-path-sum

# Dijkstra

from heapq import heappop, heappush

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        pq = [(dist[0][0],0,0)]

        while pq:
            d0,r0,c0 = heappop(pq)

            for r1,c1 in [(r0+1,c0), (r0,c0+1)]:
                if not (0 <= r1 < n and 0 <= c1 < m):
                    continue
                
                d1 = d0 + grid[r1][c1]
                if d1 < dist[r1][c1]:
                    dist[r1][c1] = d1
                    heappush(pq,(d1,r1,c1))

        return dist[-1][-1]

# recursive DP

from functools import lru_cache

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        @lru_cache(None)
        def dp(i,j):
            if i == n-1 and j == m-1:
                return grid[n-1][m-1]

            return grid[i][j] + min(dp(r,c) for (r,c) in [(i+1,j), (i,j+1)]
                                    if 0 <= r < n and 0 <= c < m)

        return dp(0,0)
    
# memoized recursive DP

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        table = [[None] * m for _ in range(n)]
        table[-1][-1] = grid[-1][-1]

        def dp(i,j):
            if table[i][j] is None:
                table[i][j] = grid[i][j] + min(dp(r,c) for (r,c) in [(i+1,j), (i,j+1)]
                                        if 0 <= r < n and 0 <= c < m)
                                        
            return table[i][j]

        return dp(0,0)
    
# for-loop DP

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        dp = [[None] * m for _ in range(n)]
        
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i == n-1 and j == m-1:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[r][c] for (r,c) in [(i+1, j), (i,j+1)] if 0 <= r < n and 0 <= c < m)

        return dp[0][0]

## DP with padding -- DO NOT implement

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        def dp(i,j):
            if i == n-1 and j == m-1:
                return grid[n-1][m-1]
            
            if not (0 <= i < n and 0 <= j < m):
                return float('inf')

            return grid[i][j] + min(dp(i+1,j), dp(i,j+1))

        return dp(0,0)

# memoization

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        table = [[None] * (m+1) for _ in range(n+1)]
        table[n-1][m-1] = grid[n-1][m-1]

        def dp(i,j):
            if table[i][j] is None:
                if not (0 <= i < n and 0 <= j < m):
                    table[i][j] = float('inf')
                else:
                    table[i][j] = grid[i][j] + min(dp(i+1,j), dp(i,j+1))
                                        
            return table[i][j]

        return dp(0,0)
    
# for-loops
    
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        dp = [[float('inf')] * (m+1) for _ in range(n+1)]
        dp[n-1][m-1] = grid[n-1][m-1]

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i == n-1 and j == m-1:
                    continue
                
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]