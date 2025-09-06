# https://leetcode.com/problems/sign-of-the-product-of-an-array

from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1

        for num in nums:
            if num < 0:
                ans = -ans
            if num == 0:
                return 0

        return ans
        