# https://leetcode.com/problems/jump-game-ii

# Dijkstra

from heapq import heappop, heappush
from functools import cache
from typing import List

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(dist[0],0)]

        while pq:
            d0,i0 = heappop(pq)

            for i1 in range(i0+1, i0+1+nums[i0]):
                if i1 >= n:
                    continue

                d1 = d0 + 1
                if d1 < dist[i1]:
                    dist[i1] = d1
                    heappush(pq,(d1,i1))

        return dist[-1]
    
# dynamic programming

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        v = [float('inf')] * n
        v[n-1] = 0

        for i in reversed(range(n - 1)):
            if nums[i] > 0:
                v[i] = 1 + min(v[i+1: i+1+nums[i]])

        return v[0]

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def v(i):
            if i == n-1:
                return 0
            if nums[i] == 0:
                return float('inf')
            return 1 + min(v(j) for j in range(i+1,i+1+nums[i]) if j < n)
    
        return v(0)
