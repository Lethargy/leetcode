# https://leetcode.com/problems/binary-search

from typing import List

# manual

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        if nums[i] == target:
            return i
        elif nums[i] > target:
            return -1
        elif nums[j] == target:
            return j
        elif nums[j] < target:
            return -1

        while j-i>1:
            m = (i+j)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                i = m
            if nums[m] > target:
                j = m
        
        return -1
    
# built-in

from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)

        if i < len(nums) and nums[i] == target:
            return i
        else:
            return -1