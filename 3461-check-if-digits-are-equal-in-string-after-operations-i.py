# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i

from itertools import pairwise

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            t = []
            for a,b in pairwise(s):
                t.append((int(a) + int(b)) % 10)
            s = ''.join(str(n) for n in t)
        
        return s[0] == s[1]