# https://leetcode.com/problems/unique-paths

# using mathematics

from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(n+m-2, n-1)
    
# pure recursive DP - DO NOT implement

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dp(i,j):
            if i == m-1 and j == n-1:
                return 1

            return sum(dp(i1,j1) for (i1,j1) in [(i+1,j), (i,j+1)]
                       if 0 <= i1 < m and 0 <= j1 < n)

        return dp(0,0)
    
# memoized recursive DP

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[None] * n for _ in range(m)] 
        table[m-1][n-1] = 1

        def dp(i,j):
            if table[i][j] is None:
                table[i][j] = sum(dp(i1,j1) for (i1,j1) in [(i+1,j), (i,j+1)]
                           if 0 <= i1 < m and 0 <= j1 < n)
            
            return table[i][j]

        return dp(0,0)