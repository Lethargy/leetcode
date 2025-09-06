# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

from functools import cache
from typing import List

# (VERSION 1) brute force recursion -- DO NOT implement

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        def b(i):
            if i >= n-1:
                return 0

            return max(b(i+1), s(i+1) - prices[i])

        def s(i):
            if i == n-1:
                return prices[i]

            return max(s(i+1), prices[i] + b(i+2))

        return b(0)
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def v(i):
            if i >= n-1:
                return 0
            return max(v(i+1), s(i+1) - prices[i])

        @cache
        def s(i):
            if i == n-1:
                return prices[i]
            return max(s(i+1), prices[i] + v(i+2))

        return v(0)
        
# (VERSION 2) tabulated form; O(n) complexity, O(n) memory
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        b = [0] * (n+1)
        s = [0] * n
        s[-1] = prices[-1]

        for i in reversed(range(n-1)):
            b[i] = max(b[i+1], s[i+1] - prices[i])
            s[i] = max(s[i+1], prices[i] + b[i+2])

        return b[0]
    
# (VERSION 3) O(n) complexity, O(1) memory
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b0 = 0
        b1 = 0
        s = prices[-1]

        for p in reversed(prices[:-1]):
            b0, b1, s = max(b0, s - p), b0, max(s, p + b1)

        return b0

