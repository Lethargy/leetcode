# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three

from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = 0
        s = 0

        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                s = s + num
                n = n + 1
        
        if n > 0:
            return s//n
        else:
            return 0
