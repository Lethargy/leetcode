# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray

from typing import List

# dynamic programming

# Let u(i) be the longest increasing sequence starting at nums[i]
# Let d(i) be the longest decreasing sequence starting at nums[i]
# u(i) = 1 + u(i+1) if nums[i] < nums[i+1] and u(i) = 1 otherwise
# d(i) = 1 + d(i+1) if nums[i] > nums[i+1] and d(i) = 1 otherwise
# Boundary condition: u(n-1) = d(n-1) = 1
# Return max(u(0),...,u(n-1),d(0),...,d(n-1))

from functools import cache

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def u(i):
            if i == n-1:
                return 1
            elif nums[i] >= nums[i+1]:
                return 1
            else:
                return 1 + u(i+1)

        @cache
        def d(i):
            if i == n-1:
                return 1
            elif nums[i] <= nums[i+1]:
                return 1
            else:
                return 1 + d(i+1)

        @cache
        def M(i):
            if i == n-1:
                return 1
            else:
                return max(M(i+1), d(i), u(i))

        return M(0)
    
# O(n) complexity, O(1) space

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        u = d = M = 1

        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                d = 1
                u = 1 + u
            elif nums[i] == nums[i+1]:
                d = 1
                u = 1
            else:
                d = 1 + d
                u = 1
            M = max(M, d, u)

        return M