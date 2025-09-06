# https://leetcode.com/problems/jump-game/

from functools import cache

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n-1

        for i in reversed(range(n-1)):
            if i + nums[i] >= last:
                last = i
        
        return last == 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dp(i):
            if i == n-1:
                return n-1

            if i + nums[i] >= dp(i+1):
                return i
            else:
                return dp(i+1)

        return dp(0) == 0