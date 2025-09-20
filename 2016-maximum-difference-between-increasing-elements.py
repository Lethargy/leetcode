# https://leetcode.com/problems/maximum-difference-between-increasing-elements

from typing import List

# dynamic programming

# Let dp(j) denote the maximum difference within nums[0],...,nums[j]
# At j, we have two options:
#   1. Settle for j as the right endpoint of the difference
#   In this case, we get nums[j] - min(nums[j-1],...,nums[0])
#   2. Skip j and go onto j-1. Then, we get dp(j-1)
# Thus, dp(j) = max(dp[j-1], nums[j] - min(nums[j-1],...,nums[0]))
# For the boundary condition, take dp(0) = 0
# Return dp(n-1) if dp(n-1) > 0 else -1

# For efficiency, let m(j) = min(nums[j],...,nums[0])
# We obtain the pair of recursions
# dp(j) = max(dp[j-1], nums[j] - m(j-1))
# m(j) = min(m(j-1), nums[j])
# with boundary condition dp(0) = 0, m(0) = nums[0]

# compare to https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# version 1
# O(n) time, O(n) space
    
from functools import cache

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:       
        n = len(nums)

        @cache
        def dp(j):
            if j == 0:
                return 0
            else:
                return max(dp(j-1), nums[j] -  m(j-1))

        @cache
        def m(j):
            if j == 0:
                return nums[j]
            else:
                return min(nums[j], m(j-1))

        return dp(n-1) if dp(n-1) > 0 else -1
    
# version 2
# O(n) time, O(n) space
    
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [None] * n
        m = [None] * n
        
        dp[0] = 0
        m[0] = nums[0]

        for j in range(1,n):
            dp[j] = max(dp[j-1], nums[j] - m[j-1])
            m[j] = min(m[j-1], nums[j])

        return dp[n-1] if dp[n-1] > 0 else -1
    
# version 3
# O(n) time, O(1) space

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:       
        dp = 0
        m = nums[0]

        for num in nums[1:]:
            dp = max(dp, num - m)
            m = min(m, num)

        return dp if dp > 0 else -1