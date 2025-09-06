# https://leetcode.com/problems/unique-paths-ii

# dynamic programming

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        @lru_cache(None)
        def dp(r,c):
            if obstacleGrid[r][c] == 1:
                return 0

            if r == n-1 and c == m-1:
                return 1

            return sum(dp(r1,c1) for (r1,c1) in [(r+1,c), (r,c+1)]
                       if 0 <= r1 < n and 0 <= c1 < m)

        return dp(0,0)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        grid = [[0] * m for _ in range(n)] # unique number of paths from (0, 0) to (i, j)
        grid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for r in range(n):
            for c in range(m):
                if obstacleGrid[r][c] == 1:
                    continue

                if r > 0:
                    grid[r][c] += grid[r-1][c]
                
                if c > 0:
                    grid[r][c] += grid[r][c-1]

        
        return grid[-1][-1]