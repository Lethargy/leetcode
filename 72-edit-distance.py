# https://leetcode.com/problems/edit-distance

from typing import List
from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def v(i,j):
            if i == -1 or j == -1:
                return max(i,j) + 1
            if word1[i] == word2[j]:
                return v(i-1,j-1)
            else:
                return 1 + min(v(i-1,j), v(i,j-1), v(i-1,j-1))

        return v(n-1,m-1)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def v(i,j):
            if i == n or j == m:
                return max(n-i,m-j)
            if word1[i] == word2[j]:
                return v(i+1,j+1)
            else:
                return 1 + min(v(i+1,j), v(i,j+1), v(i+1,j+1))

        return v(0,0)