# https://leetcode.com/problems/find-closest-number-to-zero

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = -float('inf')

        for num in nums:
            if abs(num) < abs(ans):
                ans = num
            elif abs(num) == abs(ans) and num > ans:
                ans = num
        
        return ans

        