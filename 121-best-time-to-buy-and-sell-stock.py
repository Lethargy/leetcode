# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
    
# (VERSION 1) brute force recursive DP -- DO NOT implement
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        def b(i): # best profit by buying at time i or after
            if i == n-1:
                return 0
            
            return max(b(i+1), s(i+1) - prices[i])
            
        def s(i): # best price we can sell at from day i onwards
            if i == n-1:
                return prices[n-1]
            
            return max(s(i+1), prices[i])

        return b(0)
    
## (VERSION 2) tabularized form; O(n) complexity, O(n) memory

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        b = [None] * n
        s = [None] * n
        
        b[n-1] = 0
        s[n-1] = prices[n-1]

        for i in reversed(range(n-1)):
            s[i] = max(s[i+1], prices[i])
            b[i] = max(b[i+1], s[i+1] - prices[i])

        return b[0]
    
# O(n) complexity, O(1) memory

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """      
        b = 0
        s = prices[-1]

        for p in reversed(prices[:-1]):
            s, b = max(s, p), max(b, s - p)

        return b