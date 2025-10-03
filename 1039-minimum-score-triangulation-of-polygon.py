# https://leetcode.com/problems/minimum-score-triangulation-of-polygon

from typing import List
from functools import cache
from math import inf

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        @cache
        def dp(i: int, j: int) -> int:
            if i + 1 == j:
                return 0
            
            res = inf
            for k in range(i + 1, j):
                cost = dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
                if cost < res:
                    res = cost
            return res
        
        return dp(0, n - 1)