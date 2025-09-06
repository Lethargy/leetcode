# https://leetcode.com/problems/check-if-array-is-good

from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = Counter(nums)
        n = max(nums)

        for num in range(1,n+1):
            if num < n and count[num] != 1:
                return False
            if num == n and count[num] != 2:
                return False

        return True