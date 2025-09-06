# https://leetcode.com/problems/check-if-n-and-its-double-exist

from typing import List
from itertools import pairwise

class Solution:
    def oddString(self, words: List[str]) -> str:
        def dif(s):
            return tuple(ord(b)-ord(a) for a,b in pairwise(s))

        d = dict()
        for word in words:
            t = dif(word)
            if t in d:
                d[t].append(word)
            else:
                d[t] = [word]

        for L in d.values():
            if len(L) == 1:
                return L[0]