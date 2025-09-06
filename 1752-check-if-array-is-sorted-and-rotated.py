# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[(i+1)%n] - nums[i] < 0:
                count += 1
        
        return count <= 1
        