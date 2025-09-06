# https://leetcode.com/problems/check-array-formation-through-concatenation

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lookup = {piece[0]:piece for piece in pieces}

        recreate = []
        for a in arr:
            if a in lookup:
                recreate = recreate + lookup[a]
        
        return recreate == arr
