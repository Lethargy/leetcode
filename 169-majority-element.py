# https://leetcode.com/problems/majority-element

from typing import List

# hash table

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for num,count in Counter(nums).items():
            if count > n//2:
                return num
            
# sorting

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        return nums[n//2]