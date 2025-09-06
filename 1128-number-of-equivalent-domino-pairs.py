# https://leetcode.com/problems/number-of-equivalent-domino-pairs

from typing import List
from collections import Counter
from math import comb

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter(tuple(sorted(domino)) for domino in dominoes)
        return sum(comb(count,2) for count in counts.values())