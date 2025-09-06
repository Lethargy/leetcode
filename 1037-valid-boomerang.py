# https://leetcode.com/problems/valid-boomerang

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dx1 = points[1][0]-points[0][0]
        dx2 = points[2][0]-points[0][0]
        dy1 = points[1][1]-points[0][1]
        dy2 = points[2][1]-points[0][1]

        innerProd = dx1*dx2 + dy1*dy2
        norm1squared = dx1**2 + dy1**2
        norm2squared = dx2**2 + dy2**2

        if innerProd**2 < norm1squared * norm2squared:
            return True
        else:
            return False