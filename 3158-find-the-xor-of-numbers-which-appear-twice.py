# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice

from typing import List
from collections import Counter

# hash table

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0

        for val,count in Counter(nums).items():
            if count == 2:
                ans = ans ^ val

        return ans