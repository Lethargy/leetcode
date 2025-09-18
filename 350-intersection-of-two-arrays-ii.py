# https://leetcode.com/problems/intersection-of-two-arrays-ii

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1) & Counter(nums2)
        res = []

        for num,freq in count.items():
            res += [num] * freq

        return res