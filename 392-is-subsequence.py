# https://leetcode.com/problems/is-subsequence

from functools import cache
        
# dynamic programming

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        @cache
        def dp(i,j):
            if i == n:
                return True
            if j == m:
                return False
            if s[i] == t[j]:
                return dp(i+1,j+1)
            if s[i] != t[j]:
                return dp(i,j+1)
        
        return dp(0,0)

# two pointers

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1
            
        if i == len(s):
            return True
        if j == len(t):
            return False