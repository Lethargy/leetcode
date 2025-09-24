# https://leetcode.com/problems/remove-duplicates-from-sorted-array

from typing import List

# two pointers

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0 # points to first number different from nums[i]

        while j < n:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i+1