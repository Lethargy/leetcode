# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        b = [0] * (k+1)
        s = [prices[-1]] * (k+1)

        for p in reversed(prices[:-1]):
            for i in range(1,k+1):
                b[i], s[i] = max(b[i], s[i] - p), max(s[i], p + b[i-1])

        return b[k]