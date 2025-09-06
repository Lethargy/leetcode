# https://leetcode.com/problems/coin-change

from typing import List
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float('inf')

            return 1 + min(dp(remaining - c) for c in coins)

        ans = dp(amount)
        return ans if ans < float('inf') else -1