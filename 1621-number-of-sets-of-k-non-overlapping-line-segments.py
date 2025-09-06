# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments

from functools import cache

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def V(N,K):
            if N == K or K == 0:
                return 1

            return V(N-1,K) + sum(V(I,K-1) for I in range(K-1,N))

        return V(n-1,k) % (10**9 + 7)

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def V(N,K):
            if N == K or K == 0:
                return 1

            return V(N-1,K) + S(N-1,K-1)

        @cache
        def S(N,K):
            if N == K:
                return 1
            
            return V(N,K) + S(N-1,K)

        return V(n-1,k) % (10**9 + 7)