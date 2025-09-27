# https://leetcode.com/problems/largest-triangle-area

from typing import List
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        for (x0,y0),(x1,y1),(x2,y2) in combinations(points,3):
            ans = max(ans, 0.5 * abs((x2-x0)*(y1-y0)-(x1-x0)*(y2-y0)))
        
        return ans