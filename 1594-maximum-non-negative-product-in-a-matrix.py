# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        # most positive product starting from (0,0) ending at (i,j)
        P = [[None] * m for _ in range(n)] 
        # most negative product starting from (0,0) ending at (i,j)
        N = [[None] * m for _ in range(n)]

        P[0][0] = grid[0][0]
        N[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue

                options = []
                for (r,c) in [(i-1,j),(i,j-1)]:
                    if not (0 <= r < n and 0 <= c < m):
                        continue

                    options.append(grid[i][j] * P[r][c])
                    options.append(grid[i][j] * N[r][c])

                P[i][j] = max(options)
                N[i][j] = min(options)
        
        return P[-1][-1] % (10**9 + 7) if P[-1][-1] >= 0 else -1