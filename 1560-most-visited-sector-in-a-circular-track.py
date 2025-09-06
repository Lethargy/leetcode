# https://leetcode.com/problems/most-visited-sector-in-a-circular-track

from typing import List
from itertools import pairwise

# by simulation

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count = {k+1:0 for k in range(n)}

        for a,b in pairwise(rounds):
            if a<b:
                for i in range(a,b):
                    count[i] += 1
            else:
                for i in range(a,b+n):
                    count[((i-1)%n)+1] += 1
        count[rounds[-1]] += 1

        res = []
        M = 0
        for s,c in count.items():
            if c > M:
                res = [s]
                M = c
            elif c == M:
                res.append(s)

        return res

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        if rounds[0] <= rounds[-1]:
            return list(range(rounds[0],rounds[-1]+1))
        else:
            return list(range(1,rounds[-1]+1)) + list(range(rounds[0],n+1))
