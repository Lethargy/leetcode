# https://leetcode.com/problems/find-missing-and-repeated-values

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = [1] + [0] * (n**2)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        return [count.index(2),count.index(0)]

