# https://leetcode.com/problems/stone-game-iii

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def a(i): # Alice's lead over Bob
            if i >= n:
                return 0

            return max(sum(stoneValue[i:i+X]) - b(i+X) for X in range(1,4))

        @lru_cache(None)
        def b(i): # Bob's lead over Alice
            if i >= n:
                return 0

            return max(sum(stoneValue[i:i+X]) - a(i+X) for X in range(1,4))

        A = a(0)
        if A > 0:
            return 'Alice'
        if A < 0:
            return 'Bob'
        if A == 0:
            return 'Tie'