# https://leetcode.com/problems/find-the-sum-of-encrypted-integers

from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            num = str(num)
            res += int(max(num) * len(num))
        
        return res