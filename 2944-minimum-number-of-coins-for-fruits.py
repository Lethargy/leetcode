# https://leetcode.com/problems/minimum-number-of-coins-for-fruits

from functools import cache
from typing import List

# dynamic programming

# Let dp(i) be the number of coins needed to acquire fruits i,...,n-1
# We buy fruit i and pay prices[i]
# Afterwards, we can skip any number of the next i+1 fruits
# We resume the problem at any index from i+1 (skip 0) to 2*i+2 (skip i+1)
# It follows that
# dp(i) = prices[i] + min(dp(i+1),...,dp(2*i+2)), with dp(i) = 0 if i >= n
# We return dp(0)

# O(n^2) time, O(n) space

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            return prices[i] + min(dp(k) for k in range(i+1,2*i+3))

        return dp(0)
    
# tabularized form
# O(n^2) time, O(n) space
    
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [None] * (n+1)
        dp[n] = 0
        dp[n-1] = prices[n-1]

        for i in reversed(range(n-1)):
            dp[i] = prices[i] + min(dp[k] for k in range(i+1, min(n+1,2*i+3)))

        return dp[0]
    
# using heap

# The above implementations are O(n^2) because of the minimum
# over dp(i+1),...,dp(2*i+2). We can efficiently compute this
# minimum in log(n) using a heap
# At i heap contains dp(i+1),...,dp(2*i+2)
# At i-1, heap contains dp(i),...,dp(2*i)

# O(n log n) time, O(n) space

from heap import heappop, heappush
    
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        pq = [(0,n)] # [(dp[i],i)] priority queue

        for i in reversed(range(n)):
            while pq[0][1] > 2*i+2:
                heappop(pq)
            dp = prices[i] + pq[0][0]
            heappush(pq, (dp,i))
            
        return dp