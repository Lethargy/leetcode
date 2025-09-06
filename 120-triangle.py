# https://leetcode.com/problems/triangle

# (VERSION 1) brute force recursive DP -- DO NOT implement

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        def v(i,j):
            if i == n-1:
                return triangle[n-1][j]

            return triangle[i][j] + min(v(i+1,j), v(i+1,j+1))

        return v(0,0)
        
# (VERSION 2) tabularized form; O(n^2) complexity, O(n^2) memory
    
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        v = [[None] * (i+1) for i in range(n)]
        v[n-1] = triangle[n-1]

        for i in reversed(range(n-1)):
            for j in range(i+1):
                v[i][j] = triangle[i][j] + min(v[i+1][j], v[i+1][j+1])

        return v[0][0]
        
# (VERSION 3) rewriting input; O(n^2) complexity, O(1) memory
    
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        for i in reversed(range(n-1)):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]