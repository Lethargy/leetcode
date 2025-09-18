# https://leetcode.com/problems/move-zeroes/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # points to first zero
        j = 0 # points to first nonzero after i

        while i < len(nums) and j < len(nums):
            if nums[i] != 0:
                i += 1          # find first zero
                j = max(j,i)    # j must always be right of i
            elif nums[j] == 0:
                j += 1          # find first nonzero
            else:
                nums[i], nums[j] = nums[j], nums[i]