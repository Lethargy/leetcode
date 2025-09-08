# https://leetcode.com/problems/remove-duplicates-from-sorted-array

from typing import List

# two pointers

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        for j in range(n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i+1