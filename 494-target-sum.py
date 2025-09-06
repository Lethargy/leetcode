# https://leetcode.com/problems/target-sum

# knapsack-type DP

from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        n = len(nums)

        if (S - target) % 2 != 0:
            return 0
        
        @lru_cache(None)
        def dp(r,i):
            if i < 0:
                if r == 0:
                    return 1
                else:
                    return 0

            return dp(r-nums[i],i-1) + dp(r,i-1)

        return dp((S-target)//2, n-1)