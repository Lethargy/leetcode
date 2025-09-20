# https://leetcode.com/problems/number-of-changing-keys

from itertools import pairwise

class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0

        for a,b in pairwise(s):
            if a.lower() != b.lower():
                ans += 1
        
        return ans