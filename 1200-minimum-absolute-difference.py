# https://leetcode.com/problems/minimum-absolute-difference

from typing import List
from math import inf
from itertools import pairwise

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minDiff = inf

        for a,b in pairwise(arr):
            if b-a < minDiff:
                ans = [(a,b)]
                minDiff = b-a
            elif b-a == minDiff:
                ans.append((a,b))
        
        return ans