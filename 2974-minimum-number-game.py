# https://leetcode.com/problems/minimum-number-game

from typing import List

# by sorting

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        for i in range(0,n-1,2):
            nums[i],nums[i+1] = nums[i+1],nums[i]

        return nums
        
# using heap

from heapq import heapify, heappop

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        res = []

        while nums:
            a = heappop(nums)
            b = heappop(nums)
            res.append(b)
            res.append(a)
        
        return res
        