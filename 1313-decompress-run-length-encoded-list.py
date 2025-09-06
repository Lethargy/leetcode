# https://leetcode.com/problems/decompress-run-length-encoded-list

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n//2):
            res += nums[2*i] * [nums[2*i+1]]
        
        return res
