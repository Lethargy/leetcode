# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

from typing import List

# by sorting

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowSums = [(sum(row),i) for i,row in enumerate(mat)]
        rowSums.sort()
        return [i for _,i in rowSums[:k]]