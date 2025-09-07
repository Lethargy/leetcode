# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square

from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        for l,w in rectangles:
            maxLen = max(maxLen, min(l,w))
        
        res = 0
        for l,w in rectangles:
            if min(l,w) >= maxLen:
                res += 1

        return res
