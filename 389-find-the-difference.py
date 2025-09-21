# https://leetcode.com/problems/find-the-difference

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter(Counter(t) - Counter(s)))