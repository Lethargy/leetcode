# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None] * n

        for i in range(n):
            if nums[i] % 2 == 0:
                res[i] = -1
            else:
                pos = 1
                while (nums[i] >> pos) & 1 == 1:
                    pos += 1
                res[i] = nums[i] ^ (1 << (pos - 1))
        return res