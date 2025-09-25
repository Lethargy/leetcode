# https://leetcode.com/problems/largest-number-at-least-twice-of-others

from typing import List
from heapq import nlargest

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        M,K = nlargest(2,nums)
        i = nums.index(M)

        if 2 * K <= M:
            return i
        else:
            return -1
        