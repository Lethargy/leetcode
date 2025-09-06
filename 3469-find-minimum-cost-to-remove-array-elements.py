# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements

from typing import List
from functools import cache

class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(a,i):
            if i == n-1:
                return max(a, nums[i])

            if i == n:
                return a

            b = nums[i]
            c = nums[i+1]

            return min(max(a,b) + dp(c,i+2), max(a,c) + dp(b,i+2), max(b,c) + dp(a,i+2))

        return dp(nums[0],1)