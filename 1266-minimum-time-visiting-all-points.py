# https://leetcode.com/problems/minimum-time-visiting-all-points

from typing import List
from itertools import pairwise

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for (x0,y0),(x1,y1) in pairwise(points):
            dx = abs(x0-x1)
            dy = abs(y0-y1)

            if dx < dy:
                ans += dx + (dy - dx)
            else:
                ans += dy + (dx - dy)
        
        return ans