# https://leetcode.com/problems/unique-3-digit-even-numbers

from typing import List
from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for a,b,c in permutations(digits,3):
            if a != 0 and c % 2 == 0:
                ans.add(100*a + 10*b + c)
        
        return len(ans)