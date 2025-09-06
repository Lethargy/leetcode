# https://leetcode.com/problems/stone-game

from functools import cache
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def A(i,j): # Alice's score given piles[i], ..., piles[j]
            if i == j:
                return piles[i]
            
            return max(piles[i] + B(i+1,j), piles[j] + B(i,j-1))
        
        @cache
        def B(i,j): # Bob's score given piles[i], ..., piles[j]
            if i == j:
                return piles[i]
            
            return max(piles[i] + A(i+1,j), piles[j] + A(i,j-1))

        n = len(piles)
        return A(0,n-1) > max(B(1,n-1), B(0,n-2))