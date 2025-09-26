# https://leetcode.com/problems/find-the-distinct-difference-array

from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        seenLR = set()
        uniqueLR = [None] * n
        seenRL = set()
        uniqueRL = [None] * n
        for i in range(n):
            seenLR.add(nums[i])
            uniqueLR[i] = len(seenLR)
            seenRL.add(nums[~i])
            uniqueRL[~i] = len(seenRL)

        for i in range(n-1):
            uniqueLR[i] -= uniqueRL[i+1]
        
        return uniqueLR