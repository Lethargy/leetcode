# https://leetcode.com/problems/array-partition

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        for i,n in enumerate(nums):
            if i % 2 == 0:
                ans = ans + n
            
        return ans
    
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])