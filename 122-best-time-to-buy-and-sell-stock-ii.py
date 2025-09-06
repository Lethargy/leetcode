# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def v(i):
            if i == n-1:
                return 0
            return max(v(i+1), M(i+1) - prices[i])
        
        @cache
        def M(i):
            if i == n-1:
                return prices[n-1]
            return max(M(i+1), prices[i] + v(i+1))

        return v(0)

# (VERSION 2) tabularized form; O(n) complexity, O(n) memory
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        v = [None] * n
        M = [None] * n

        v[n-1] = 0
        M[n-1] = prices[n-1]

        for i in reversed(range(n-1)):
            v[i] = max(v[i+1], M[i+1] - prices[i])
            M[i] = max(M[i+1], prices[i] + v[i+1])
        
        return v[0]

    
# (VERSION 3) O(n) complexity, O(1) memory
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        v = 0
        M = prices[-1]

        for p in reversed(prices[:-1]):
            v, M = max(v, M - p), max(M, p + v)
        
        return v