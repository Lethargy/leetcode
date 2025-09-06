# https://leetcode.com/problems/height-checker

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        ans = 0

        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                ans = ans + 1
        
        return ans