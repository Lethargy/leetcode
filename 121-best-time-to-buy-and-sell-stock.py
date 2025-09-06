# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
    
from functools import cache
from typing import List

# attempt 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def v(i):
            if i == n-1:
                return 0

            return max(v(i+1), max(prices[i+1:]) - prices[i])

        return v(0)
    
# solution 1

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
            return max(M(i+1), prices[i])

        return v(0)
    
# solution 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        v = [None] * n
        M = [None] * n

        v[n-1] = 0
        M[n-1] = prices[n-1]

        for i in reversed(range(n-1)):
            v[i] = max(v[i+1], M[i+1] - prices[i])
            M[i] = max(M[i+1], prices[i])

        return v[0]    

# solution 3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        v = 0
        M = prices[n-1]

        for p in reversed(prices[:-1]):
            v = max(v, M - p)
            M = max(M, p)

        return v