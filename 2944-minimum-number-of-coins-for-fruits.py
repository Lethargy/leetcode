# https://leetcode.com/problems/minimum-number-of-coins-for-fruits

from functools import cache
from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def v(i):
            if i >= n:
                return 0
            
            return prices[i] + min(v(k) for k in range(i+1,2*i+3))

        return v(0)
    
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        v = [None] * (n+1)
        v[n] = 0
        v[n-1] = prices[n-1]

        for i in reversed(range(n-1)):
            v[i] = prices[i] + min(v[k] for k in range(i+1, min(n+1,2*i+3)))

        return v[0]