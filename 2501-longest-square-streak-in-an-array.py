# https://leetcode.com/problems/longest-square-streak-in-an-array

from typing import List
from functools import cache
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squares = set(num for num in nums if sqrt(num) == int(sqrt(num)))

        @cache
        def v(n):
            if n**2 not in squares:
                return 1
            
            return 1 + v(n**2)
        
        ans = max(v(n) for n in nums)
        return ans if ans >= 2 else -1