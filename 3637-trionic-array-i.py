# https://leetcode.com/problems/trionic-array-i

from typing import List
from itertools import pairwise

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) == 3:
            return False

        if nums[0] > nums[1]:
            return False

        turns = 0
        direction = 'up'

        for a,b in pairwise(nums):
            if direction == 'up' and b < a:
                turns += 1
                direction = 'down'
            elif direction == 'down' and b > a:
                turns += 1
                direction = 'up'
            elif a == b:
                return False
        
        return turns == 2

        