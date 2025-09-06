# https://leetcode.com/problems/coin-change-ii

# knapsack-type DP

from functools import lru_cache

class Solution:
    def change(self, amount, coins):
        @lru_cache(None)
        def v(n,i):
            if i == 0:
                return int(n % coins[0] == 0)

            if n == 0:
                return 1
            
            if n < 0:
                return 0

            return v(n - coins[i], i) + v(n, i-1)

        return v(amount, len(coins)-1)