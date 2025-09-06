# https://leetcode.com/problems/maximum-subarray

from typing import List
from functools import cache

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def v(i):
            if i == n-1:
                return nums[n-1]
            
            return nums[i] + max(v(i+1), 0)

        return max(v(i) for i in range(n))

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        v = [None] * n
        v[n-1] = nums[n-1]

        for i in reversed(range(n-1)):
            v[i] = nums[i] + max(v[i+1], 0)

        return max(v)
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        v = nums[n-1]
        M = nums[n-1]

        for i in reversed(range(n-1)):
            v = nums[i] + max(v, 0)
            M = max(M, v)

        return M