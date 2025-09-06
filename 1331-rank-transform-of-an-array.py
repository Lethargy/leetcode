# https://leetcode.com/problems/rank-transform-of-an-array/

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        i = 1
        rank = dict()

        for num in sorted(arr):
            if num not in rank:
                rank[num] = i
                i += 1
        
        return [rank[num] for num in arr]