# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        return sum(minNum < num < maxNum for num in nums)
        