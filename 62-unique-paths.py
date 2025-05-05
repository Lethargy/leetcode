# https://leetcode.com/problems/unique-paths

from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(n+m-2, n-1)