# https://leetcode.com/problems/count-pairs-of-similar-strings

from typing import List
from math import comb
from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = Counter()

        for word in words:
            count[frozenset(word)] += 1

        return sum(comb(n,2) for n in count.values() if n >= 2)
            
            