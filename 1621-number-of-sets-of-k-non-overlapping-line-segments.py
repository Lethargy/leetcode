# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments

from functools import cache

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def v(n,k):
            if n == k or k == 0:
                return 1

            return v(n-1,k) + sum(v(i,k-1) for i in range(k-1,n))

        return v(n-1,k) % (10**9 + 7)

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def v(n,k):
            if n == k+1 or k == 0:
                return 1

            return v(n-1,k) + s(n-1,k-1)

        @cache
        def s(n,k):
            if n == k+1:
                return 1
            
            return v(n,k) + s(n-1,k)

        return v(n,k) % (10**9 + 7)
