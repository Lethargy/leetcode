# https://leetcode.com/problems/maximum-average-subarray-i

from typing import List

# sliding window

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        S = M = sum(nums[:k])

        for i in range(k,len(nums)):
            S = S + nums[i] - nums[i-k]
            M = max(M, S)
        
        return M / k