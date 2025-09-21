# https://leetcode.com/problems/count-elements-with-maximum-frequency

from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = 0
        maxCount = 0
        for c in count.values():
            if c > maxCount:
                maxCount = c
                res = c
            elif c == maxCount:
                res += c
        
        return res