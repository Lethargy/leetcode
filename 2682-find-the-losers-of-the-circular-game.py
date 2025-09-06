# https://leetcode.com/problems/find-the-losers-of-the-circular-game

from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        count = [0] * n
        i = 1
        p = 0
        count[p] = M = 1

        while M < 2:
            p = (p + i*k) % n
            count[p] += 1
            M = max(M, count[p])
            i += 1
            
        return [k+1 for k in range(n) if count[k] == 0]
