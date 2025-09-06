# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string

from collections import Counter
from itertools import pairwise

class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)

        for n,m in pairwise(s):
            if n != m and count[n] == int(n) and count[m] == int(m):
                return n + m
        
        return ''