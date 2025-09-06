# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

# (VERSION 1) brute force recursive DP -- DO NOT implement

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        def b(i,k):
            if i == n-1:
                return 0
            
            if k == 0:
                return 0

            return max(b(i+1,k), s(i+1,k) - prices[i])
        
        def s(i,k):
            if i == n-1:
                return prices[n-1]
            
            if k == 0:
                return 0

            return max(s(i+1,k), prices[i] + b(i+1,k-1))

        return b(0,2)
    
# (VERSION 2) tabularized form; O(n) complexity, O(n) memory
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        b = [[0] * 3 for _ in range(n)]
        s = [[0] * 3 for _ in range(n)]
        s[n-1] = [prices[n-1]] * 3

        for i in reversed(range(n-1)):
            for k in [1,2]:
                b[i][k] = max(b[i+1][k], s[i+1][k] - prices[i])
                s[i][k] = max(s[i+1][k], prices[i] + b[i+1][k-1])

        return b[0][2]
    
# (VERSION 3) O(n) complexity, O(1) memory
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = [0] * 3
        s = [prices[-1]] * 3

        for p in reversed(prices[:-1]):
            for k in [1,2]:
                b[k], s[k] = max(b[k], s[k] - p), max(s[k], p + b[k-1])

        return b[2]