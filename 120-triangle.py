# https://leetcode.com/problems/triangle

from typing import List
from functools import cache

# (VERSION 1) recursive dp

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        @cache
        def v(i,j):
            if i == n-1:
                return triangle[n-1][j]
            else:
                return triangle[i][j] + min(v(i+1,j), v(i+1,j+1))

        return v(0,0)
        
# (VERSION 2) tabularized form; O(n^2) complexity, O(n^2) memory
    
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        v = [[None] * (i+1) for i in range(n)]
        v[n-1] = triangle[n-1]

        for i in reversed(range(n-1)):
            for j in range(i+1):
                v[i][j] = triangle[i][j] + min(v[i+1][j], v[i+1][j+1])

        return v[0][0]
        
# (VERSION 3) rewriting input; O(n^2) complexity, O(1) memory
    
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in reversed(range(n-1)):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]