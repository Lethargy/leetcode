# https://leetcode.com/problems/longest-alternating-subarray

from typing import List
from functools import cache

# dynamic programming
# Let u(i) be the longest "up" subarray starting at i (nums[i] < nums[i+1])
# Let d(i) be the longest "down" subarray starting at i (nums[i] > nums[i+1])


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def u(i): # longest "up" subarray starting at i
            if i < n-1 and nums[i+1] == nums[i] + 1:
                return 1 + d(i+1)
            else:
                return 1

        @cache
        def d(i): # longest "down" array starting at i
            if i < n-1 and nums[i+1] == nums[i] - 1:
                return 1 + u(i+1)
            else:
                return 1

        @cache
        def M(i):
            if i == n-1:
                return u(n-1)
            else:
                return max(u(i),M(i+1))

        return M(0) if M(0) > 1 else -1

# tabularization

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        u = [None] * n
        d = [None] * n
        M = [None] * n

        u[n-1] = 1
        d[n-1] = 1
        M[n-1] = 1

        for i in reversed(range(n-1)):
            if nums[i+1] == nums[i] + 1:
                u[i] = 1 + d[i+1]
                d[i] = 1
            elif nums[i+1] == nums[i] - 1:
                u[i] = 1
                d[i] = 1 + u[i+1]
            else:
                u[i] = 1
                d[i] = 1
            M[i] = max(u[i],M[i+1])

        return M[0] if M[0] > 1 else -1

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        u = d = M = 1

        for i in reversed(range(n-1)):
            if nums[i+1] == nums[i] + 1:
                u, d = 1+d, 1
            elif nums[i+1] == nums[i] - 1:
                u, d = 1, 1+u
            else:
                u, d = 1, 1
            M = max(u,M)
            
        return M if M > 1 else -1








