# https://leetcode.com/problems/divide-array-into-equal-pairs

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for val in Counter(nums).values():
            if val % 2 != 0:
                return False
        
        return True
        