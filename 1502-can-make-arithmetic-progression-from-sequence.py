# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

from typing import List
from itertools import pairwise

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for a,b in pairwise(arr):
            if b-a != diff:
                return False
        
        return True