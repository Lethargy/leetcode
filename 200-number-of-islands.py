# https://leetcode.com/problems/number-of-islands/description


# DFS iterative

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        k = len(grid[0])
        ans = 0

        def dfs(i,j):
            stack = [(i,j)]

            while stack:
                r0,c0 = stack.pop()
                grid[r0][c0] = '0'

                for r1,c1 in [(r0+1,c0), (r0-1,c0), (r0,c0-1), (r0,c0+1)]:
                    if not (0 <= r1 < n and 0 <= c1 < k):
                        continue

                    if grid[r1][c1] == '1':
                        stack.append((r1,c1))
        
        for i in range(n):
            for j in range(k):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans = ans + 1

        return ans