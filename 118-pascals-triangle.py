# https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        v = [[1] * (k+1) for k in range(numRows)]
        
        for i in range(2,numRows):
            for j in range(1,i):
                v[i][j] = v[i-1][j-1] + v[i-1][j]

        return v