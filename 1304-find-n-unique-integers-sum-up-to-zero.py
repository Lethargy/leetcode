# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        if n % 2 == 1:
            res.append(0)
            n = n-1
        
        for k in range(n//2):
            res.append(k+1)
            res.append(-(k+1))
        
        return res