# https://leetcode.com/problems/count-the-hidden-sequences/description

class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        min0 = 0
        max0 = 0
        s = 0
        n = len(differences)

        for i in range(n):
            s = s + differences[i]
            min0 = min(min0, s)
            max0 = max(max0, s)

        
        return max(1 + (upper - lower) - (max0 - min0), 0)
