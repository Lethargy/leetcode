# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i

from typing import List

# O(n) time, O(1) space

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxNum = 0
        maxDiff = 0
        res = 0

        for num in nums:
            res = max(res, maxDiff * num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)
        
        return res


