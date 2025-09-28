# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements

from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(reverse = True)
        return nums[:k]