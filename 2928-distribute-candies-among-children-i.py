# https://leetcode.com/problems/distribute-candies-among-children-i

from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        C0 = comb(n+2,2)
        C1 = comb(n+2-limit-1,2) if limit + 1 <= n else 0
        C2 = comb(n+2-2*(limit + 1),2) if 2*(limit + 1) <= n else 0
        C3 = comb(n+2-3*(limit + 1),2) if 3*(limit + 1) <= n else 0

        return C0 - 3*C1 + 3*C2 - C3