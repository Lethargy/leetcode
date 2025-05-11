# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

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