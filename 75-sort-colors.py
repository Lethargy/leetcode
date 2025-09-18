# https://leetcode.com/problems/sort-colors

from typing import List

# two pointers

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # everything left of i should be 0
        j = len(nums)-1 # everything right of j should be 2
        p = 0 # pointer, always between i and j

        while p <= j: # should be i <= p <= j, but i <= p is always true
            if nums[i] == 0: # if i points to 0, increase i
                i += 1
                p = max(p,i)
            elif nums[j] == 2: # if j points to 2, decrease j
                 j -= 1
            elif nums[p] == 0: # if p points to 0, swap with value at i
                nums[i], nums[p] = nums[p], nums[i]
            elif nums[p] == 2: # if p points to 2, swap with value at j
                nums[j], nums[p] = nums[p], nums[j]
            elif nums[p] == 1: # if p points to 1, increase p
                p += 1
                
# hash tables

from collections import Counter                

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        count = Counter(nums)

        zeros = count[0]
        ones = count[1]
        twos = count[2]

        for i in range(zeros):
            nums[i] = 0

        for i in range(zeros,zeros+ones):
            nums[i] = 1
        
        for i in range(zeros+ones,zeros+ones+twos):
            nums[i] = 2