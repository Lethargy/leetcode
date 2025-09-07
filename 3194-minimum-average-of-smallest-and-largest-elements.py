# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements

from typing import List
from math import inf

# sorting, two pointers
# O(n) time, O(1) space

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        res = inf

        for i in range(n//2):
            res = min(res, 0.5 * (nums[i] + nums[~i]))
        
        return res