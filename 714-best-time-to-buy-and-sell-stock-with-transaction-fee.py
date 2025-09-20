# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

from typing import List

# dynamic programming

# version 1
# O(n) time, O(n) space

from functools import cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def b(i):
            if i == n-1:
                return 0
            return max(b(i+1), s(i+1) - prices[i])
        
        @cache
        def s(i):
            if i == n-1:
                return 0
            return max(s(i+1), prices[i] - fee + b(i+1))

        return b(0)
    
# version 2
# O(n) time, O(n) space
    
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        b = [None] * n
        s = [None] * n

        b[n-1] = 0
        s[n-1] = prices[n-1] - fee

        for i in reversed(range(n-1)):
            b[i] = max(b[i+1], s[i+1] - prices[i])
            s[i] = max(s[i+1], prices[i] - fee + b[i+1])

        return b[0]
    
# version 3
# O(n) time, O(1) space

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b = 0
        s = prices[-1] - fee

        for price in reversed(prices[:-1]):
            b,s = max(b, s - price), max(s, price - fee + b)

        return b