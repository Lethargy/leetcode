# https://leetcode.com/problems/maximum-ascending-subarray-sum

from typing import List

# O(n) time, O(1) space

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = res = S = nums[0] 

        for num in nums[1:]:
            if num > prev:
                S += num
                res = max(res, S)
            else:
                S = num
            prev = num
        
        return res
