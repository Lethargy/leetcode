# https://leetcode.com/problems/positions-of-large-groups/description/

from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        i = 0
        j = 0
        res = []

        while j <= n:
            if j == n and j-i >= 3:
                res.append([i,j-1])
                break
            elif j == n:
                break
            elif s[i] == s[j]:
                j += 1
            elif j-i >= 3:
                res.append([i,j-1])
                i = j
            else:
                i = j

        return res