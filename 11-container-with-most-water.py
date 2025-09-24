# https://leetcode.com/problems/container-with-most-water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1

        area = min(height[i],height[j]) * (j-i)

        while i<j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            area = max(area, min(height[i],height[j]) * (j-i))
        
        return area