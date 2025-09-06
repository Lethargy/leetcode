# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description

from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        n = len(grid)
        m = len(grid[0])
        
        queue = deque([(0,0,health - grid[0][0])])
        seen = set((0,0,health - grid[0][0]))

        while queue:
            i,j,h = queue.popleft()

            if i == n-1 and j == m-1 and h > 0:
                return True

            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0 <= r < n and 0 <= c < m):
                    continue
                
                h1 = h - grid[r][c]

                if h1 <= 0 or (r,c,h1) in seen:
                    continue

                queue.append((r,c,h1))
                seen.add((r,c,h1))
                
        return False