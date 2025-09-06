# https://leetcode.com/problems/find-subarrays-with-equal-sum

from typing import List
from itertools import pairwise

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for a,b in pairwise(nums):
            if a+b in seen:
                return True
            else:
                seen.add(a+b)
        
        return False