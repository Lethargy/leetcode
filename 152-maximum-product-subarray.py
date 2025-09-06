# https://leetcode.com/problems/maximum-product-subarray

from typing import List

# pure recursive DP -- DO NOT implement

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        def p(i): # most positive product starting at i
            if i == N-1:
                return nums[-1]
            return max(nums[i], nums[i] * p(i+1), nums[i] * n(i+1))

        def n(i): # most negative product starting at i
            if i == N-1:
                return nums[-1]
            return min(nums[i], nums[i] * p(i+1), nums[i] * n(i+1))

        return max(p(i) for i in range(N))
        
# tabularized form; O(n) complexity, O(n) memory
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        P = [None] * n # most positive product starting at i
        N = [None] * n # most negative product starting at i

        P[n-1] = nums[n-1]
        N[n-1] = nums[n-1]

        for i in reversed(range(n-1)):
            P[i] = max(nums[i], nums[i] * P[i+1], nums[i] * N[i+1])
            N[i] = min(nums[i], nums[i] * P[i+1], nums[i] * N[i+1])

        return max(P)
    
# O(n) complexity, O(1) memory

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        P = nums[n-1]
        N = nums[n-1]
        ans = nums[n-1]

        for i in reversed(range(n-1)):
            P, N = max(nums[i], nums[i] * P, nums[i] * N), min(nums[i], nums[i] * P, nums[i] * N)
            ans = max(ans, P)

        return ans
        