# https://leetcode.com/problems/stone-game-ii

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def a(i,M): # Alice's lead over Bob
            if i >= n:
                return 0

            return max(sum(piles[i:i+X]) - b(i+X,max(M,X)) for X in range(1,2*M+1))

        @lru_cache(None)
        def b(i,M): # Bob's lead over Alice
            if i >= n:
                return 0

            return max(sum(piles[i:i+X]) - a(i+X,max(M,X)) for X in range(1,2*M+1))
        
        return (a(0,1) + sum(piles)) // 2 # number of stones that Alice has