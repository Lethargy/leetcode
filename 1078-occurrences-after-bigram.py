# https://leetcode.com/problems/occurrences-after-bigram

from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        n = len(words)

        res = []
        for i in range(n-1):
            if words[i] == first and words[i+1] == second and i+2 < n:
                res.append(words[i+2])

        return res