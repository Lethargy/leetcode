# https://leetcode.com/problems/count-hills-and-valleys-in-an-array

from typing import List
from itertools import pairwise

# O(n) time, O(1) space 

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        direction = None
        directionChanges = 0

        for a,b in pairwise(nums):
            if a < b and direction != 'up':
                direction = 'up'
                directionChanges += 1
            elif a > b and direction != 'down':
                direction = 'down'
                directionChanges += 1
        
        return max(0, directionChanges - 1)