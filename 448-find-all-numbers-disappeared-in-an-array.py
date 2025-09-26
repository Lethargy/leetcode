# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return list(set(range(1,n+1)) - set(nums))