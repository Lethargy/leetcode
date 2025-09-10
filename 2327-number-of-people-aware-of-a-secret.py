# https://leetcode.com/problems/number-of-people-aware-of-a-secret

# dynamic programming
# let dp(i) = number of new people who learn the secret on day i
# dp(i) = dp(i-delay) + ... + dp(i - (forget-1))
# dp(1) = 1
# dp(i) = 0 for i < 1
# return dp(n) + dp(n-1) + ... + dp(n-(forget-1))

from functools import cache

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 1
            if i <= 0:
                return 0
            return sum(dp(i-k) for k in range(delay,forget))
        
        return sum(dp(n-k) for k in range(forget)) % (10**9 + 7)

# using queues

from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = deque([0]*forget)
        dp[-1] = 1
        s = 0
        for i in range(1,n):
            s += dp[-delay]
            s -= dp.popleft()
            dp.append(s)
        
        return sum(dp)%(10**9+7)
    
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = deque([0]*forget)
        dp[0] = 1
        s = 0
        for i in range(1,n):
            s -= dp.pop()
            s += dp[delay-1]
            dp.appendleft(s)
        
        return sum(dp)%(10**9+7)