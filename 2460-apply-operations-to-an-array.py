# https://leetcode.com/problems/apply-operations-to-an-array

from typing import List

# O(n) time, O(n) space

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        res = [num for num in nums if num > 0]
        return res + [0] * (n - len(res))
    
# two pointers
# O(n) time, O(1) space
    
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        i = 0 # first zero
        j = 0 # first nonzero after i
        while i < n and j < n:
            while i < n and nums[i] != 0:
                i += 1
            j = max(j,i)
            while j < n and nums[j] == 0:
                j += 1
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1

        return nums