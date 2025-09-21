# https://leetcode.com/problems/maximum-ascending-subarray-sum

from typing import List
from functools import cache

# dynamic programming with backwards recursion

# Let dp(i) be the best sum starting at i.
# If nums[i] < nums[i+1], then dp(i) = nums[i] + dp(i+1)
# Otherwise, dp(i) = nums[i]
# Boundary condition: dp(n-1) = nums[n-1]
# Return max(dp(0),...,dp(n-1))
# Define M(i) = max(dp(i),M(i+1)) to compute max(dp(i),...,dp(n-1))

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            if i == n-1:
                return nums[i]
            elif nums[i+1] > nums[i]:
                return nums[i] + dp(i+1)
            else:
                return nums[i]
        
        @cache
        def M(i):
            if i == n-1:
                return dp(i)
            else:
                return max(M(i+1),dp(i))

        return M(0)

# tabularized for-loop: O(n) time, O(n) space

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [None] * n
        M = [None] * n

        dp[n-1] = nums[n-1]
        M[n-1] = nums[n-1]

        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                dp[i] = nums[i] + dp[i+1]
            else:
                dp[i] = nums[i]
            M[i] = max(dp[i], M[i+1])

        return M[0]
    
# overwriting variables: O(n) time, O(1) space
    
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        dp = nums[n-1]
        M = nums[n-1]

        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                dp = nums[i] + dp
            else:
                dp = nums[i]
            M = max(dp, M)

        return M

# dynamic programming with forward recursion

# Let dp(i) be the best sum ending at i.
# If nums[i] > nums[i-1], then dp(i) = nums[i] + dp(i-1)
# Otherwise, dp(i) = nums[i]
# Boundary condition: dp(0) = nums[0]
# Return max(dp(0),...,dp(n-1))
# Define M(i) = max(M(i-1),dp(i)) to compute max(dp(0),...,dp(i))

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            if i == 0:
                return nums[0]
            elif nums[i] > nums[i-1]:
                return nums[i] + dp(i-1)
            else:
                return nums[i]
        
        @cache
        def M(i):
            if i == 0:
                return dp(i)
            else:
                return max(M(i-1),dp(i))

        return M(n-1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [None] * n
        M = [None] * n

        dp[0] = nums[0]
        M[0] = nums[0]

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
            M[i] = max(M[i-1], dp[i])

        return M[n-1]

# O(n) time, O(1) space
    
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        dp = nums[0]
        M = nums[0]

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp = nums[i] + dp
            else:
                dp = nums[i]
            M = max(M, dp)

        return M

# The "computer science approach"

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