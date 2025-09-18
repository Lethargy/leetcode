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

# ChatGPT5's solution

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:  # Need at least 4 elements to form three parts
            return False

        i = 0
        # Step 1: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        p = i
        if p == 0 or p == n - 1:
            return False

        # Step 2: strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        q = i
        if q == p or q == n - 1:
            return False

        # Step 3: strictly increasing again
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1

        

        