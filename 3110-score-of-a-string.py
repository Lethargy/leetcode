# https://leetcode.com/problems/score-of-a-string

from itertools import pairwise

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0

        for a,b in pairwise(s):
            ans += abs(ord(a)-ord(b))

        return ans