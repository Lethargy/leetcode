# https://leetcode.com/problems/sort-array-by-parity-ii

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0 # always points to even index
        j = 1 # always points to odd index

        while i < n and j < n:
            if nums[i] % 2 == 0: # find first "wrong" i value
                i += 2
            elif nums[j] % 2 == 1: # find first "wrong" j value
                j += 2
            else: # now that both i and j are wrong, switch them
                nums[i], nums[j] = nums[j], nums[i]
        
        return nums