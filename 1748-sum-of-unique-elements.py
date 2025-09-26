# https://leetcode.com/problems/sum-of-unique-elements

from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0

        for num,count in Counter(nums).items():
            if count == 1:
                ans += num

        return ans