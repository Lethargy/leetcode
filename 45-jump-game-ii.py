# https://leetcode.com/problems/jump-game-ii

# Dijkstra

from heapq import heappop, heappush

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

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        J = [float('inf')] * n
        J[-1] = 0

        for i in reversed(range(n - 1)):
            if nums[i] > 0:
                J[i] = 1 + min(J[i+1: i+1+nums[i]])

        return J[0]
    
# pure recursive DP - DO NOT implement

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def dp(i):
            if i == n-1:
                return 0
            
            if nums[i] == 0:
                return float('inf')

            return 1 + min(dp(j) for j in range(i+1,i+1+nums[i]) if j < n)
    
        return dp(0)

# recursive DP with memoization

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        table = [None] * n
        table[-1] = 0

        def dp(i):
            if table[i] is not None:
                return table[i]
            
            if nums[i] == 0:
                table[i] = float('inf')
            else:
                table[i] = 1 + min(dp(j) for j in range(i+1,i+1+nums[i]) if j < n)
                
            return table[i]
    
        return dp(0)