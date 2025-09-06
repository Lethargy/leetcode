# https://leetcode.com/problems/number-of-1-bits

# dynamic programming

from functools import cache

class Solution:
    def hammingWeight(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            return 1 + dp(i & (i-1))
        
        return dp(n)
    
# efficient
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            n,r = n//2, n%2
            ans = ans + r
        
        return ans