# https://leetcode.com/problems/house-robber-ii

from typing import List


# Consider the first problem: (https://leetcode.com/problems/house-robber)
# Run this algorithm on houses 0,...,n-2 and then 1,...,n-1, and take the larger

from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        @cache
        def dp1(i):
            if i == n-2:
                return nums[n-2]
            elif i == n-1:
                return 0
            else:
                return max(nums[i] + dp1(i+2), dp1(i+1))
        
        @cache
        def dp2(i):
            if i == n-1:
                return nums[n-1]
            elif i == n:
                return 0
            else:
                return max(nums[i] + dp2(i+2), dp2(i+1))
        
        return max(dp1(0), dp2(1))