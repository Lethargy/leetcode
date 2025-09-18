# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid

from typing import List

# iterating over rows

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])

        for row in grid:
            for i,num in enumerate(row):
                ans[i] = max(ans[i], len(str(num)))
        
        return ans

# iterating over columns

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []

        for col in zip(*grid): # transposes the matrix
            ans.append(max(len(str(num)) for num in col))

        return ans
