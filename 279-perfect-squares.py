# https://leetcode.com/problems/perfect-squares

from math import sqrt
from functools import cache

# recursive dynamic programming

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [(k+1)**2 for k in range(int(sqrt(n)))]

        @cache
        def dp(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            return 1 + min(dp(rem - s) for s in squares)
        
        return dp(n)
    
# BFS
    
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # list all squares that could add up to n
        # example: for n = 12, we get squares = [1, 4, 9]
        squares = [(k+1)**2 for k in range(int(sqrt(n)))]

        # start "layer" count
        count = 0
        queue = {n}
        
        while queue:
            next_queue = {q-s for q in queue for s in squares if s <= q}
            # if queue = {12}, then next_queue = {11,8,3}
            # (obtained by subtracting off 1, 4, and 9 from 12)
            # set is used instead of list to avoid duplicates
            
            count = count + 1

            # if we find 0 in next queue, we're done
            if 0 in next_queue:
                return count

            # otherwise, we continue
            queue = next_queue.copy()