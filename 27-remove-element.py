# https://leetcode.com/problems/remove-element

from typing import List

# two pointers

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0 # points to val
        j = 0 # points to first non-val right of i
        
        while j < n:
            if nums[i] != val:
                i += 1
                j = max(j,i)
            elif nums[j] == val:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        return i