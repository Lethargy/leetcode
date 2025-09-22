# https://leetcode.com/problems/house-robber

from typing import List
from functools import cache

# dynamic programming

# Let dp(i) denote the most money we can earn from houses i,...,n-1
# We have two options:
#   1. Rob house i. Then we earn nums[i] but give up house i+1,
#   and restart the problem at house i+2. We get nums[i] + dp(i+2).
#   2. Pass up house i. We get dp(i+1).
# It follows that dp(i) = max(dp(i+1), nums[i] + dp(i+2)).
# Boundary conditions: dp(n-1) = nums[n-1] and dp(n) = 0

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):                
            if i == n-1:
                return nums[n-1]
            elif i == n:
                return 0
            else:
                return max(dp(i+1), nums[i] + dp(i+2))

        return dp(0)
    
# tabularized; O(n) time, O(n) memory
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None] * (n+1)
        dp[n-1] = nums[n-1]
        dp[n] = 0

        for i in reversed(range(n-1)):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        return dp[0]
    
# O(n) complexity, O(1) memory
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp0 = nums[n-1]
        dp1 = 0

        for num in reversed(nums[:-1]):
            dp0, dp1 = max(dp0, num + dp1), dp0

        return dp0