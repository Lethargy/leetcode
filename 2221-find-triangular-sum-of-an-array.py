# https://leetcode.com/problems/find-triangular-sum-of-an-array

from typing import List
from itertools import pairwise

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = []
            for a,b in pairwise(nums):
                newNums.append((a+b)%10)
            nums = newNums
        
        return nums[0]