# https://leetcode.com/problems/find-the-middle-index-in-array

from typing import List

# prefix sum

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        S = sum(nums)

        prefixSum = 0
        for i,num in enumerate(nums):
            if prefixSum + nums[i] == S - prefixSum:
                return i
            prefixSum += num

        return -1
    
# more elegant approach
    
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = 0
        suffixSum = sum(nums)

        for i,num in enumerate(nums):
            suffixSum -= num
            if prefixSum == suffixSum:
                return i
            prefixSum += num

        return -1