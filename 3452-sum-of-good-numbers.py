# https://leetcode.com/problems/sum-of-good-numbers

from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            if i+k < n and nums[i+k] >= nums[i]:
                continue
            elif i-k >= 0 and nums[i-k] >= nums[i]:
                continue
            res += nums[i]
        
        return res
        