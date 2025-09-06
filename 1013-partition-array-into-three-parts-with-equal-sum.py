# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum

from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        S = sum(arr)

        if S % 3 != 0:
            return False
    
        n = len(arr)
        prefix = 0
        prefixEnd = None
        for k,num in enumerate(arr):
            prefix += num
            if 3*prefix == S:
                prefixEnd = k
                break

        suffix = 0
        suffixStart = None
        for k,num in enumerate(reversed(arr)):
            suffix += num
            if 3*suffix == S:
                suffixStart = n-1-k
                break
        
        if prefixEnd is None or suffixStart is None:
            return False

        return suffixStart-prefixEnd > 1


