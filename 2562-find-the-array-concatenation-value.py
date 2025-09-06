# https://leetcode.com/problems/find-the-array-concatenation-value

from typing import List

# two pointers

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        value = 0
        i = 0
        j = len(nums)-1

        while i < j:
            value += int(str(nums[i]) + str(nums[j]))
            i = i + 1
            j = j - 1

        if i == j:
            value += nums[i]
        
        return value