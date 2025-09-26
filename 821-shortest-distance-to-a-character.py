# https://leetcode.com/problems/shortest-distance-to-a-character

from typing import List
from functools import cache
from math import inf

# dynamic programming

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)

        @cache
        def L(i):
            if i == n:
                return inf
            elif s[i] == c:
                return 0
            else:
                return 1 + L(i+1)
        
        @cache
        def R(i):
            if i == -1:
                return inf
            elif s[i] == c:
                return 0
            else:
                return 1 + R(i-1)

        return [min(L(i),R(i)) for i in range(n)]