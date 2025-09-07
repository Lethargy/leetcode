# https://leetcode.com/problems/set-mismatch

from typing import List

# O(n) time, O(n) space

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [1] + [0] * len(nums)

        for num in nums:
            count[num] += 1
        
        return [count.index(2), count.index(0)]