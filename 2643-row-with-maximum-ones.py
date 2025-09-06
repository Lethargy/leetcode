# https://leetcode.com/problems/row-with-maximum-ones

from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [float('inf'), -float('inf')]

        for i,row in enumerate(mat):
            ones = sum(row)
            if ones > res[1]:
                res[0] = i
                res[1] = ones
        
        return res
