# https://leetcode.com/problems/integer-replacement

from functools import cache

class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def v(k):
            if k == 1:
                return 0
            
            if k % 2 == 0:
                return 1 + v(k//2)
            else:
                return 1 + min(v(k+1),v(k-1))

        return v(n)