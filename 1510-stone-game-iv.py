# https://leetcode.com/problems/stone-game-iv

from typing import List
from functools import lru_cache
from math import sqrt

# fails to time constraint

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def a(k):
            s = int(sqrt(k))

            if s**2 == k:
                return True

            return not all(b(k-i**2) for i in range(1,s+1))

        @lru_cache(None)
        def b(k):
            s = int(sqrt(k))

            if s**2 == k:
                return True

            return not all(a(k-i**2) for i in range(1,s+1))

        return a(n)

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        a = [False] * (n+1)
        b = [False] * (n+1)

        for i in range(1,int(sqrt(n))+1):
            a[i] = True
            b[i] = True

        for k in range(1,n+1):
            s = int(sqrt(k))
            a[k] = not all(b[k-i**2] for i in range(1,s+1))
            b[k] = not all(a[k-i**2] for i in range(1,s+1))

        return a[n]
